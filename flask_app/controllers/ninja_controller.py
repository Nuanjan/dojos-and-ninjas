from flask_app import app
from flask import redirect, render_template, session, request, url_for
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/add_ninja')
def add_ninja():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_dojos=all_dojos)


@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    print(request.form, ": my request form")
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninja.create_ninja(data)
    return redirect('/')
