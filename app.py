import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

cloudinary.config(
    cloud_name=os.environ.get("CLOUD_NAME"),
    api_key=os.environ.get("API_KEY"),
    api_secret=os.environ.get("API_SECRET")
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reviews")
def reviews():
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))
    return render_template("login.html")


@app.route("/log_out")
def log_out():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))
    return render_template("logout.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        backlogs = list(mongo.db.backlog.find({"added_by": username}))
        finish = list(mongo.db.finished.find({"added_by": username}))
        reviews = list(mongo.db.reviews.find({"review_by": username}))
        return render_template(
            "profile.html", username=username,
            backlogs=backlogs, finish=finish, reviews=reviews)
    return redirect(url_for("log_in"))


@app.route("/add_backlog", methods=["GET", "POST"])
def add_backlog():
    if request.method == "POST":
        backlog = {
            "backlog_name": request.form.get("backlog_name"),
            "added_by": session["user"]
        }
        mongo.db.backlog.insert_one(backlog)
        flash("Game Successfully Added")
        redirect(url_for("profile", username=session["user"]))
    backlogs = mongo.db.backlog.find().sort("backlog_name", 1)
    return render_template("add_backlog.html", backlogs=backlogs)


@app.route("/edit_backlog/<backlog_id>", methods=["GET", "POST"])
def edit_backlog(backlog_id):
    if request.method == "POST":
        submit = {
            "backlog_name": request.form.get("backlog_name"),
            "added_by": session["user"]
        }
        mongo.db.backlog.update({"_id": ObjectId(backlog_id)}, submit)
        flash("Game Successfully Updated")

    backlog = mongo.db.backlog.find_one({"_id": ObjectId(backlog_id)})
    backlogs = mongo.db.backlog.find().sort("backlog_name", 1)
    return render_template(
        "edit_backlog.html", backlog=backlog, backlogs=backlogs)


@app.route("/delete_backlog/<backlog_id>")
def delete_backlog(backlog_id):
    mongo.db.backlog.remove(
        {"_id": ObjectId(backlog_id)})
    flash("Game Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))

# WHEN FINSHED I WANT TO ADD
# THIS TO ANOTHER COLLECTION,
# AND THE REMOVE IT FROM THE CURRENT ONE
# IT GET REMOVED, BUT NOT INSERTED
# TO THE OTHER COLLECTION


@app.route("/finished_backlog/<backlog_id>")
def finished_backlog(backlog_id):
    move = mongo.db.backlog.find_one(
        {"_id": ObjectId(backlog_id)})
    mongo.db.finished.insert(move)
    mongo.db.backlog.remove(
        {"_id": ObjectId(backlog_id)})
    flash("Congratulations on finishing the game")
    return redirect(
        url_for("profile", username=session["user"]))


@app.route("/add_finished", methods=["GET", "POST"])
def add_finished():
    if request.method == "POST":
        finished = {
            "backlog_name": request.form.get("backlog_name"),
            "added_by": session["user"]
        }
        mongo.db.finished.insert_one(finished)
        flash("Game Successfully Added")
        redirect(url_for("profile", username=session["user"]))
    finish = mongo.db.finished.find().sort("backlog_name", 1)
    return render_template("add_finished.html", finish=finish)


@app.route("/add_review/<finished_id>", methods=["GET", "POST"])
def add_review(finished_id):
    if request.method == "POST":
        photo = request.files['photo_url']
        photo_upload = cloudinary.uploader.upload(photo)
        review = {
            "review_name": request.form.get("review_name"),
            "genre_name": request.form.get("genre_name"),
            "platform_name": request.form.get("platform_name"),
            "developer_name": request.form.get("developer_name"),
            "duration": request.form.get("duration"),
            "review_text": request.form.get("review_text"),
            "rating_nr": request.form.get("rating_nr"),
            "photo_url": photo_upload["secure_url"],
            "review_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("reviews"))

    finished = mongo.db.finished.find_one({"_id": ObjectId(finished_id)})
    finish = mongo.db.finished.find().sort("backlog_name", 1)
    genres = mongo.db.reviews_genre.find().sort("genre_name", 1)
    platforms = mongo.db.reviews_platform.find().sort("platform_name", 1)
    ratings = mongo.db.rating.find().sort("rating_nr", 1)
    return render_template(
        "add_review.html", finished=finished, finish=finish,
        genres=genres, platforms=platforms, ratings=ratings)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        photo = request.files['photo_url']
        photo_upload = cloudinary.uploader.upload(photo)
        submit = {
            "review_name": request.form.get("review_name"),
            "genre_name": request.form.get("genre_name"),
            "platform_name": request.form.get("platform_name"),
            "developer_name": request.form.get("developer_name"),
            "duration": request.form.get("duration"),
            "review_text": request.form.get("review_text"),
            "rating_nr": request.form.get("rating_nr"),
            "photo_url": photo_upload["secure_url"],
            "review_by": session["user"]
        }
        mongo.db.reviews.update({"_id":ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")

    review = mongo.db.reviews.find_one({"_id":ObjectId(review_id)})
    genres = mongo.db.reviews_genre.find().sort("genre_name", 1)
    platforms = mongo.db.reviews_platform.find().sort("platform_name", 1)
    ratings = mongo.db.rating.find().sort("rating_nr", 1)
    return render_template(
        "edit_review.html", review=review, genres=genres, platforms=platforms, ratings=ratings)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
