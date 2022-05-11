from flask import Flask, render_template, request, redirect
# import the class from user.py
from user import User
app = Flask(__name__)

# ! CREATE
@app.route('/users/new')
def new_user():
    return render_template("new.html")

@app.route("/create/user", methods=['POST'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')

# ! READ  
@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)

@app.route("/users/<int:id>")
def show(id):
    data = {'id': id }
    user = User.get_one(data)
    print(user)
    return render_template("show.html", user = user)

# ! UPDATE

@app.route("/users/<int:id>/edit")
def edit(id):
    data = {'id': id }
    user = User.get_one(data)
    return render_template("edit.html", user = user)

@app.route("/edit/user", methods=['POST'])
def handle_edit():
    print(request.form)
    User.update(request.form)
    return redirect('/')

# ! DELETE

@app.route("/users/<int:id>/delete")
def destroy(id):
    data = {'id': id}
    User.destroy(data)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)