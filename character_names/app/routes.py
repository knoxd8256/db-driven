from app import app
from flask import render_template, flash, redirect
from . import nameGen
from app.forms import NameForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Home")

@app.route('/genPage')
def genPage():
    names = nameGen.arrGen(20)
    return render_template("generator.html", title="Generator", names=names)
    
@app.route('/charAdder', methods=['GET', 'POST'])
def charAdder():
    form = NameForm()
    if form.validate_on_submit():
        nameGen.titles.append(form.title.data)
        nameGen.names.append(form.name.data)
        nameGen.descriptors.append(form.descriptor.data)
        flash('Added {} {} the {}'.format(
            form.name.data, form.title.data, form.descriptor.data))
        return redirect('/index')
    return render_template('charadder.html', title='Character Adder', form=form)