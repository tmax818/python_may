import re
from flask_app import app
from flask import render_template,redirect,request,session,flash

from flask_app.models.user import User


## TODO creates the root route of the app and displays all users
@app.route('/')
@app.route('/users')
def index():
    users = User.get_all()
    return render_template('index.html', users = users)

## TODO Show the new user form
@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

## TODO handle new user form
@app.route('/create/user', methods=['POST'])
def create_user():
    print(request.form)
    user = User.save(request.form)
    print(user)
    return redirect(f"/users/{user}")

## TODO route to user show page
@app.route('/users/<int:id>')
def show_user(id):
    data = {'id':id}
    user = User.get_one(data)
    return render_template('show_user.html', user = user)

## TODO route to edit user form
@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {'id': id}
    user = User.get_one(data)
    return render_template('edit_user.html', user = user)

## TODO handle user edit
@app.route('/edit/user', methods=['POST'])
def update_user():
    print(request.form)
    user = User.update(request.form)
    print(user)
    return redirect(f"/users/{request.form['id']}")

@app.route('/delete/<int:id>')
def destroy_user(id):
    data = {'id':id}
    User.destroy(data)
    return redirect('/')
