from flask import Flask, render_template, redirect, request, session

from flask_login import LoginManager
login_manager = LoginManager()

from database import Family
from database import Recipe
from database import Fridge
from database import Vote

from peewee import fn

app = Flask(__name__)
app.secret_key = "yumaru"

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def top():
    recipe3 = Recipe.select().where(Recipe.grade == "普通").order_by(fn.Random()).limit(3)
    luxury3 = Recipe.select().where(Recipe.grade == "高級").order_by(fn.Random()).limit(3)
    return render_template("top.html", recipe3=recipe3, luxury3=luxury3)

@app.route("/kion")
def kion():
    import requests
    API_KEY = "9cd74ab89d6d419ead82cc94b83fa670"
    url = f"https://api.weatherbit.io/v2.0/current?lat=39.688096271304325&lon=141.1645963703204&lang=ja&units=M&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    kion = data["data"][0]["app_temp"]
    return render_template("kion.html", kion=kion)

@app.route("/vote")
def vote():
    fridge3 = Fridge.select().order_by(fn.Random()).limit(3)
    user_name = session["user_name"]
    return render_template("vote.html", fridge3=fridge3, user_name=user_name)

@app.route("/vote2", methods=["post"])
def vote2():
    name = session["user_name"]
    what = request.form["what"]
    vote = Vote(
        name=name,
        what = what,
    )
    vote.save()
    return redirect("/")

@app.route("/need")
def need():
    return render_template("need.html")

@app.route("/check")
def check():
    return render_template("check.html")

@app.route("/recommend")
def recommend():
    return render_template("recommend.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/register", methods=["post"])
def register():
    name = request.form["name"]
    mailaddress = request.form["mailaddress"]
    password = request.form["password"]
    allergie = request.form["allergie"]
    family = Family(
        name=name,
        mailaddress = mailaddress,
        password = password,
        allergie = allergie
    )
    family.save()
    return redirect("/")

@app.route("/buy")
def buy():
    return render_template("buy.html")

@app.route("/buy2")
def buy2():
    return render_template("buy2.html")

@app.route("/buy3")
def buy3():
    return render_template("buy3.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/login", methods=["post"])
def login():
    mailaddress = request.form["mailaddress"]
    password = request.form["password"]
    family = Family.select().where(Family.mailaddress==mailaddress, Family.password==password).first()
    if family is None:
        return redirect("/signin")
    session["user_name"] = family.name
    return redirect("/")

@app.route("/otamesi")
def otamesi():
    namae="ゆうまる"
    namae2="レイマル"
    return render_template("お試し.html",abc=namae,aaa=namae2)

app.run(debug=True, host="0.0.0.0", port=5001)