import os
import datetime

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # This query creates a table to keep track of purchases
    db.execute("CREATE TABLE IF NOT EXISTS purchase (SN INTEGER PRIMARY KEY, user_id INTEGER, symbol TEXT, stock TEXT, shares INTEGER, current_price NUMERIC, time NUMERIC)")

    # This query allows me to check recent purchases of user
    rowa = db.execute("SELECT symbol, stock, SUM(shares), current_price FROM purchase WHERE user_id = (?) GROUP BY stock", session["user_id"])

    # This query checks for current price of the stocks purchased by user by using lookup() and then updates the old prices
    for row in rowa:
        db.execute("UPDATE purchase SET current_price = (?) WHERE stock = (?)", lookup(row["symbol"])["price"], row["stock"])

    # The essence of this query is to allow access to the new updated prices
    rows = db.execute("SELECT symbol, stock, SUM(shares), current_price FROM purchase WHERE user_id = (?) GROUP BY stock", session["user_id"])

    # This query allows me know user's remaining cash
    user_info = db.execute("SELECT * FROM users WHERE id = (?)", session["user_id"])

    # User's remaining cash
    cash = user_info[0]["cash"]

    # If the user has made zero purchases, render this version of index.html template
    if len(rows) < 1:
        info = False
        return render_template("index.html", info=info, cash=usd(cash))

    # Else user has made purchases
    else:
        info = True
        money = 0

        for row in rows:
            money += (row["current_price"] * row["SUM(shares)"])

        money += cash

        return render_template("index.html", rows=rows, info=info, cash=usd(cash), money=usd(money))



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # If request is GET, just get the page
    if request.method == "GET":
        return render_template("buy.html")

    # Else (meyhod is POST), get details from page
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        #Ensure symbol is submitted
        if not symbol:
            return apology("You must input a symbol")

        #Ensure symbol is a vaild symbol
        sym = lookup(symbol)
        if sym == None:
            return apology("No such symbol")

        # Ensure shares is submitted
        if not shares:
            return apology("You must input shares to buy")

        # Ensure shares is a positive integer
        if float(shares) < 1 or float(shares) % 1 != 0:
            return apology("Shares must be a positive integer")

        # Company stock information
        company = lookup(symbol)

        # Know how much user has
        rows = db.execute("SELECT * FROM users WHERE id = (?)", session["user_id"])

        # If user's cash can afford shares he oredred
        if float(rows[0]["cash"]) >= (float(shares) * company["price"]):

            rem_cash = float(rows[0]["cash"]) - (float(shares) * company["price"])

            db.execute("UPDATE users SET cash = (?) WHERE id = (?)", rem_cash, session["user_id"])

            db.execute("CREATE TABLE IF NOT EXISTS purchase (SN INTEGER PRIMARY KEY, user_id INTEGER, symbol TEXT, stock TEXT, shares INTEGER, current_price NUMERIC, time NUMERIC)")

            # Timestamp
            time = datetime.datetime.now().isoformat()

            db.execute("INSERT INTO purchase (user_id, symbol, stock, shares, current_price, time) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], company["symbol"], company["name"], shares, lookup(company["symbol"])["price"], time)


            return redirect("/")

        # User does not have enough cash
        else:
            return apology("Not enough cash")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # if method is "GET", show this page
    if request.method == "GET":
        return render_template("quote.html")

    # else (method is "POST"), submit details typed in input fields
    else:
        # Get detail
        symbol = request.form.get("symbol")

        # Ensure a symbol is submitted
        if not symbol:
            return apology("Input a symbol")

        # Lookup quote of symbol
        sym = lookup(symbol)

        # If symbol doesn't exist
        if sym == None:
            return apology("No such symbol")

        # Display stock quote
        return render_template("quoted.html", sym=sym)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # if method is "GET", just show the page
    if request.method == "GET":
        return render_template("register.html")

    # else (method is "POST"), submit details typed in input fields
    else:

        # get details from page
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("You must input a username")

        # Ensure username has not already been taken
        users = db.execute("SELECT * FROM users WHERE username = (?)", username)
        for line in users:
            if line["username"] == username:
                return apology("This username is already taken")

        # Ensure password was submitted
        if not password:
            return apology("You must provide a password")

        # Ensure confirmation password was submitted
        if not confirmation:
            return apology("Please confirm password")

        # Ensure password and confirmation are the same
        if not password == confirmation:
            return apology("Passwords do not match")

        # Register user
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
        return redirect("/login")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)










