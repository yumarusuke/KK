from flask import Flask, render_template, redirect, request

from flask_login import LoginManager
login_manager = LoginManager()

from database import Family
from database import Recipe

from peewee import fn

app = Flask(__name__)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def top():
    recipe3 = Recipe.select().order_by(fn.Random()).limit(3)
    return render_template("top.html", recipe3=recipe3)

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
    return render_template("vote.html")

@app.route("/buy")
def buy():
    return render_template("buy.html")

@app.route("/cold")
def cold():
    return render_template("cold.html")

@app.route("/suggest")
def suggest():
    return render_template("suggest.html")

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

@app.route("/food")
def food():
    return render_template("food.html")

@app.route("/food2")
def food2():
    return render_template("food2.html")

@app.route("/food3")
def food3():
    return render_template("food3.html")

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
    return redirect("/")

@app.route("/otamesi")
def otamesi():
    namae="ゆうまる"
    namae2="レイマル"
    return render_template("お試し.html",abc=namae,aaa=namae2)

app.run(debug=True, host="0.0.0.0", port=5001)