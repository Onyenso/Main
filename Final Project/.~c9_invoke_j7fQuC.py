import secrets
from cs50 import SQL
import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

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


# Configure session to use filesystem (instead of signed cookies)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")



"""For Badges"""
def badges():
    # Friend request details
    fr_rq_details = db.execute("SELECT * FROM ? WHERE declined = 0 ", f'{session["username"]} friends')
    badge = len(fr_rq_details)
    if badge == 0:
        badge = ""

    friend_rqs = {"rqs": fr_rq_details, "badges": badge}
    return friend_rqs




@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Must provide username!", "danger")
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):

            flash("Must provide password!", "danger")
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM database WHERE username = :username", username = request.form.get("username").capitalize())
        # Query database for email
        if len(rows) != 1:
            rows = db.execute("SELECT * FROM database WHERE email =:email", email = request.form.get("username").lower())

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            flash("Invalid username and/or password!", "danger")
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]
        session["email"] = rows[0]["email"]


        flash("Logged in!", "success")

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")




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
        email = request.form.get("email").lower()
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure username was submitted
        if not username:
            flash("Must provide username!", "danger")
            return apology("You must input a username")

        if not email:
            flash("Must provide an email!", "danger")
            return apology("You must input an email")

        # Ensure username and emial has not already been taken
        users = db.execute("SELECT * FROM database WHERE username = ?", username)
        for line in users:
            if line["username"].lower() == username.lower():
                flash("This username is already taken.", "danger")
                return apology("This username is already taken")

            if line["email"].lower() == email.lower():
                flash("This email is already taken.", "danger")
                return apology("This email is already taken")

        # Ensure password was submitted
        if not password:
            flash("Must provide password!", "danger")
            return apology("You must provide a password")

        # Ensure confirmation password was submitted
        if not confirmation:
            flash("Please confirm password!", "danger")
            return apology("Please confirm password")

        # Ensure password and confirmation are the same
        if not password == confirmation:
            flash("PasswordS do not match!", "danger")
            return apology("Passwords do not match")

        # Register user
        db.execute("INSERT INTO database (username, email, password) VALUES (?, ?, ?)", username, email, generate_password_hash(password))


        # Create table for user's friends and friend requests. When accepted, the accepted coloumn will get updated to 1 else the friend will remain 0
        db.execute("CREATE TABLE IF NOT EXISTS ? (id INTEGER FORIEGN KEY REFERENCES database(id), username TEXT, accepted INTEGER DEFAULT 0 NOT NULL, time_fr NUMERIC, time_accepted NUMERIC DEFAULT 0 NOT NULL, declined INTEGER DEFAULT 0)", f"{username} friends")

        flash(f'Account created for {username}.', 'success')
        return redirect("/login")


@app.route("/")
@login_required
def index():
    """Show friend list of user"""
    friends = db.execute("SELECT * FROM ? WHERE accepted = 1", f'{session["username"]} friends')
    return render_template("index.html", friends=friends, badges=badges(), user=session["username"])



# Function for saving profie picture
def save_picture(form_picture):
    # Randomize filename to be sure filename doesn't already exist
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)

    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)
    return picture_fn







@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    """Show user account info"""
    # If get method is GET
    if request.method == "GET":

        image_file = db.execute("SELECT * FROM database WHERE id = ?", session["user_id"])

        if image_file[0]["image"] == "default.jpg":
            image_file[0]["image"] = url_for("static", filename='profile_pics/'+'default.jpg')


        return render_template("account.html", badges=badges(), image_file=image_file[0]["image"])

    # If method is POST
    else:
        username = request.form.get("username").capitalize()
        email = request.form.get("email").lower()
        pic = request.form.get("pic")


        users = db.execute("SELECT * FROM database WHERE username = ?", username)

        # If email was updated, run checks with database
        if (username != session["username"] and username != "") or (email != session["email"] and email !=""):
            for line in users:
                if line["username"].lower() == username.lower():
                    flash("This username is already taken.", "danger")
                    return apology("This username is already taken")

                if line["email"].lower() == email.lower():
                    flash("This email is already taken.", "danger")
                    return apology("This email is already taken")

        # If email was updated, run checks

        # I found no shorter way to do this, please bear with me
        if username:
            db.execute("UPDATE database SET username = ? WHERE username = ?", username, session["username"])
            # Rename user's friends table
            db.execute("ALTER TABLE ? RENAME TO ?", f'{session["username"]} friends', f'{username} friends')
            
            session["username"] = username

        if email:
            db.execute("UPDATE database SET email = ? WHERE username = ?", email, session["username"])
            session["email"] = email

        # If profile picture was updated
        if pic:
            root, ext = os.path.splitext(pic.filename)
            # If file is not an image
            if ext not in [".jpeg", ".jpg", ".png"]:
                flash("Upload only files of .jpeg, .jpg and ,png externsions.", "danger")
                return apology("Invalid file type.")

            picture_file = save_picture(pic)
            db.execute("UPADTE database SET image = ? WHERE id = ?", picture_file, session["user_id"])


        flash("Account info upadted", "success")
        return redirect("/account")





@app.route("/add_friend", methods=["GET", "POST"])
@login_required
def add():

    # If method = GET
    if request.method == "GET":

        return render_template("add.html", badges=badges(), user=session["username"])

    # Method is Post
    else:
        username = request.form.get("username").capitalize()

        # If username was not typed in
        if not username:
            flash("Please input a username!", "danger")
            return apology("Please input a username")

        # Check for new friend in general database
        rows = db.execute("SELECT * FROM database WHERE username = (?)", username)


        # If friend username was not found on YensoGram
        if len(rows) != 1:

            flash("Username is not on Yensogram. Please check username again.", "danger")
            return apology("Username is not on Yensogram. Please check username again.")

        # If friend username was found on YensoGram
        for row in rows:

            # If user tried to add himself as a friend
            if row["username"].lower() == session["username"].lower():
                flash("You can't add yourself as a friend.", "danger")
                return apology("You can't add yourself as a friend.")

        # Check if user already has the username as a friend
        check = db.execute("SELECT * FROM ? WHERE username = (?)", f'{session["username"]} friends', rows[0]["username"])
        if len(check) == 1:
            flash("You already have this user as a friend.", "danger")
            return apology("You already have this user as a friend.")

        # Send request to friend
        #db.execute("INSERT INTO ? (username, time) VALUES (?, datetime('now'))", f'{rows[0]["username"]} friend requests', session["username"])

        # Insert user into friend's friend list but unaccepted
        db.execute("INSERT INTO ? (id, username, time_fr) VALUES ((SELECT id FROM database WHERE username = ?), ?, datetime('now'))", f'{rows[0]["username"]} friends', session["username"], session["username"])

        # Insert friend into user's freind list but unaccepted
        db.execute("INSERT INTO ? (id, username, time_fr, declined) VALUES ((SELECT id FROM database WHERE username = ?), ?, datetime('now'), NULL)", f'{session["username"]} friends', rows[0]["username"], rows[0]["username"])

        flash("Request sent.", "success")
        return redirect("/")


# Create route for user's friend requests
@app.route("/friend_requests")
@login_required
def friend_request():
    # Show friend requests
    return render_template("friend_rqs.html", friend_rqs=badges(), badges=badges(), user=session["username"])



# Create route for accepting friend requests
@app.route("/friend_requests_accept/<friend>")
@login_required
def friend_request_accept(friend):

    # Update user's friend list and add friend by setting accepted to 1
    db.execute("UPDATE ? SET accepted = 1, time_accepted = datetime('now'), declined = NULL WHERE username = ?", f'{session["username"]} friends', friend.capitalize())

    # Update friends's friend list and add user by setting accepted to 1
    db.execute("UPDATE ? SET accepted = 1, time_accepted = datetime('now') WHERE username = ?", f'{friend} friends', session["username"].capitalize())


    return redirect("/friend_requests")



# Create route for declining friend requests
@app.route("/friend_requests_decline/<friend>")
@login_required
def friend_request_decline(friend):

    # Update user's friend list and "delete" friend by setting declined to 1
    db.execute("UPDATE ? SET declined = 1 WHERE username = ?", f'{session["username"]} friends', friend.capitalize())

    return redirect("/friend_requests")



# Create route accouts for every user on YensoGram. This route shows messages between searcher and user.
@app.route("/<some_user>", methods=["GET", "POST"])
# You have to be looged in to see your messages with such user
@login_required
def user(some_user):

    if request.method == "GET":

        # Check if the searched person(some_user) has an account on YG.
        rows = db.execute("SELECT * FROM database WHERE username = ?", some_user.capitalize())

        # If searched person(some_user) is not on YG:
        if len(rows) != 1:
            return render_template('info.html', user=session["username"], badges=badges(), info="There is no such user on YensoGram with the URL you provided.")

        # The searched person is on YG
        else:

            # Check if the person is friends with the user
            lines = db.execute("SELECT * FROM ? WHERE username = ?", f'{session["username"]} friends', some_user.capitalize())

            # If searched person is not friends with the user
            if len(lines) != 1:
                return render_template("info.html", user=session["username"], badges=badges, info=f"You are not friends with this user. Add {some_user} as a friend to see your messages.")

            # Searched person is friends with user, so show  their messages together
            return render_template("messages.html", badges=badges(), user=session["username"], some_user=some_user)

    """ Create two table of messages for any user -recieved messages and sent messages. When getting the page use request.args.get to get
    the message and insert it into some_user"s recieved messages databse. When postin to the page use request.form.get to get the message and insert into seesion["useranme]'s
    sent messages database."""

    return "TODO"



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
        flash(f"{e.name}!", "danger")
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)








