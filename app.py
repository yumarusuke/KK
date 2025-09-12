from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("top.html")

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

@app.route("/otamesi")
def otamesi():
    namae="ゆうまる"
    namae2="レイマル"
    return render_template("お試し.html",abc=namae,aaa=namae2)

app.run(debug=True, host="0.0.0.0", port=5001)