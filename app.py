from flask import Flask, render_template, redirect, request, session

from flask_login import LoginManager
login_manager = LoginManager()

from database import Family
from database import Recipe
from database import Fridge
from database import Vote
from database import Shohin

from peewee import fn

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = "yumaru"

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def top():
    if session.get("user_name") is None:
        return redirect("/signin")
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


@app.route("/vote")
def vote():
    name = session["user_name"]
    fridge3 = Fridge.select().order_by(fn.Random()).limit(3)
    import datetime
    today = datetime.date.today()
    votes = Vote.select(Vote.what, fn.COUNT(Vote.id).alias('count')).where(Vote.when == today).group_by(Vote.what)
    return render_template("vote.html", fridge3=fridge3,name=name,votes=votes)

@app.route("/need")
def need():
    return render_template("need.html")

@app.route("/needer", methods=["post"])
def needer():
    import pytesseract
    import cv2
    import numpy as np
    from PIL import Image
    # img = Image.open("static/IMG_4750.jpg")
    file = request.files["file"]
    file2 = request.files["file2"]
    file3 = request.files["file3"]
    file4 = request.files["file4"]
    if file.filename == "":
        return "ファイルが選択されていません", 400
    img_bytes = file.read()

    npimg = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY +  cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(gray, lang="jpn")
    from google import genai
    client = genai.Client(api_key= os.environ.get("API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"以下のTesseractで画像から文字にしたものを、綺麗なHTMLにしてみやすくしてください。なおHTMLのコードのbodyタグの中身だけ出してください。前後の「```」は要りません。{text}"
    )
    print(response.text)
    return render_template("need.html", receipt=response.text)

@app.route("/check")
def check():
    return render_template("check.html")

@app.route("/suggest")
def suggest():
    shohin = Shohin.select()
    names = [s.name for s in Shohin.select(Shohin.name)]
    print(names)
    from google import genai
    client = genai.Client(api_key= os.environ.get("API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""この中の食材を何個か使って一週間分の献立を作ってください。また、食材が偏らないようにバランスよく作ってください。そして,"<div class="card" style="width: 18rem;">
  <img src="/static/[曜日].png" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">唐揚げ</h5>
    <p class="card-text">今日のご飯は</p>
 <a href="https://cookpad.com/jp/search/%E5%94%90%E6%8F%9A%E3%81%92?event=search.suggestion&order=recent" target="_blank">クックパッド：唐揚げ</a>
  </div>"のような形式で表示してください。なおHTMLのコードのbodyタグの中身だけ出してください。{names}"""
    )
    print(response.text)
    return render_template("suggest.html", menu=response.text)

@app.route("/index")
def index():
    return render_template("index.html")

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


@app.route("/食材選択")
def 食材選択():
    return render_template("食材選択.html")

@app.route("/食材選択2")
def 食材選択2():
    return render_template("食材選択2.html")

@app.route("/食材選択3")
def 食材選択3():
    return render_template("食材選択3.html")

@app.route("/map")
def map():
    return render_template("map.html")


@app.route("/お試し２")
def お試し２():
    return render_template("お試し２.html")

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