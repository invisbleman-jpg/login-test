from flask import Flask, render_template, redirect, request, url_for, session # type: ignore

app = Flask(__name__)
app.secret_key = "8Mdfk2kfm2kf2)e3=üs"


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    session["log"] = False
    if request.method == "POST":
        username_inp = request.form["username"]
        password_inp = request.form["password"]
        if username_inp == "invisbleman" and password_inp == "pormp678":
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