from flask import Flask, render_template, redirect, request, url_for, session # type: ignore
from cryptography.fernet import Fernet #type:ignore
import json

with open("secret_key.key", "r") as f:
    key = f.read().encode("utf-8")

fernet = Fernet(key)

k = json.load(open("user.JSON"))

app = Flask(__name__)
app.secret_key = "8Mdfk2kfm2kf2)e3=üs"

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():

    session["log"] = False
    if request.method == "POST":
        username_inp = request.form["username"]
        password_inp = request.form["password"]

        username, password = fernet.decrypt(((k["user"][0]["username"]).encode("utf-8"))), fernet.decrypt(((k["user"][1]["password"]).encode("utf-8")))


        if username_inp == username.decode("utf-8") and password_inp == password.decode("utf-8"):

        
            session["username"] = username_inp
            session["log"] = True 
            return redirect(url_for("home"))
        

    return render_template("index.html")
@app.route("/home")
def home():
    if session.get("log") == True:
        return "login successful"
    else:
        return redirect(url_for("index"))