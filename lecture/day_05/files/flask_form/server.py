from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "some secret key"

# ! our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

# ! our create_user route will handle the input from our form
@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)
    print((request.environ))
    session['ip'] = request.remote_addr
    session['form_data'] = request.form['data']
    session['user_name'] = request.form['user_name']11
    return redirect('/')

    
if __name__ == "__main__":
    app.run(debug=True)