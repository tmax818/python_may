from flask import Flask, render_template, request, redirect
# import the class from user.py
from user import User
app = Flask(__name__)


@app.route('/users/new')
def new_user():
    return render_template("new.html")

@app.route("/create/user", methods=['POST'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')
            
@app.route("/")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)


if __name__ == "__main__":
    app.run(debug=True)