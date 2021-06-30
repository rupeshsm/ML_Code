import re
from flask import Flask, render_template, request

app = Flask(__name__)

DEPT = [
    "COMP",
    "INFT",
    "EXTC",
    "ELEC"
]
@app.route('/')


def index():
    return render_template("index.html", departement = DEPT)



@app.route('/welcome', methods =["post"])
def welcome():
    if not request.form.get("name") or not request.form.get("departement"):
        return render_template("faliure.html")
    return render_template("welcome.html", name = request.form.get("name","World" ))



