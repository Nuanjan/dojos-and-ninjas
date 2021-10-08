from flask_app import app
from flask import redirect, render_template, session, request, url_for
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def all_dojos():
    all_dojos = Dojo.get_all()
    return render_template('index.html', all_dojos=all_dojos)


@app.route('/add_dojo', methods=['POST'])
def add_dojo():
    print(request.form['name'])
    data = {
        "name": request.form['name']
    }
    Dojo.add_dojo(data)
    return redirect('/dojos')


@app.route('/dojo/<int:dojo_id>')
def show_dojo_and_ninjas(dojo_id):
    data = {
        "dojo_id": dojo_id
    }
    ninja_list = Dojo.get_dojo_with_ninja(data)
    print(ninja_list.ninja, " this is ninja_list")
    return render_template('ninja_list.html', ninja_list=ninja_list)
