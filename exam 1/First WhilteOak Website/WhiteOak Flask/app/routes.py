from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", css="index", title="Home")

@app.route('/about')
def about():
    return render_template("about.html", css="about", title="About Us")

@app.route('/classes')
def classes():
    return render_template("classes.html", css="classes", title="Classes")

@app.route('/solutions')
def solutions():
    return render_template("solutions.html", css="solutions", title="Solutions")