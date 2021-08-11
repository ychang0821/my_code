#!/usr/bin/python3

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/start")
def start():
    return render_template("trivia_example.html")

@app.route("/correct/<answer>")
def correct(answer):
    return f"{answer} is correct!"

@app.route("/check", methods = ["POST"])
def check():
    if request.form.get("an") and request.form.get("an").lower() == "soccer":
        return redirect(url_for("correct", answer = request.form.get("an").lower()))

    elif request.json.get("an") and request.json.get("an").lower() == "soccer":
        return redirect(url_for("correct", answer = request.json.get("an").lower()))
    else:
        return redirect(url_for("start")) 
    

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)