import os
import datetime

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, usd

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



@app.route("/")
@login_required
def index():
    """Show friend list of user"""

    friends = db.execute("SELECT * FROM ?", session["username"])

    return render_template("index.html", friends=friends, user=session["username"])
    



@app.route("/add_friend", methods=["GET", "POST"])
@login_required
def add():

    # If method = GET
    if request.method == "GET":
        return render_template("add.html")

    # Method is Post
    else:
        username = request.form.get("username").capitalize()

        # If username was not typed in
        if not username:
            return apology("Please input a username")

        # Check for new friend in general database
        rows = db.execute("SELECT * FROM database WHERE username = (?)", username)


        # If friend username was not found on YensoGram
        if len(rows) != 1:
            return apology("Username is not on Yensogram. Please check username again.")

        # If friend username was found on YensoGram
        for row in rows:
            # If user tried to add himself as a friend
            if row["username"].lower() == session["username"].lower():
                return apology("You can't add yourself as a friend.")

        # Check if user already has the username as a friend
        check = db.execute("SELECT * FROM ? WHERE username = (?)", session["username"], rows[0]["username"])
        if len(check) == 1:
            return apology("You already have this user as a friend.")

        time = datetime.datetime.now().isoformat()

        # Insert new friend into user's database
        db.execute("INSERT INTO ? (username, time) VALUES (?, ?)", session["username"], username, time)

        return redirect("/")



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
        rows = db.execute("SELECT * FROM database WHERE username = :username", username=request.form.get("username").capitalize())

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

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


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # if method is "GET", just show the page
    if request.method == "GET":
        return render_template("register.html")

    # else (method is "POST"), submit details typed in input fields
    else:

        # get details from page
        username = request.form.get("username").capitalize()
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            return apology("You must input a username")

        # Ensure username has not already been taken
        users = db.execute("SELECT * FROM database WHERE username = (?)", username)
        for line in users:
            if line["username"].lower() == username.lower():
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
        db.execute("INSERT INTO database (username, hash) VALUES (?, ?)", username, generate_password_hash(password))

        # Create table for user to keep track of friends and time added as friends
        db.execute("CREATE TABLE IF NOT EXISTS ? (id INTEGER PRIMARY KEY, username TEXT, time NUMERIC)", username)
        return redirect("/login")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)










