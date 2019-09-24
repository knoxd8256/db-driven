from app import app
from flask import render_template
from . import nameGen

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Home")

@app.route('/genPage')
def genPage():
    names = nameGen.arrGen(20)
    return render_template("generator.html", title="Generator", names=names)
