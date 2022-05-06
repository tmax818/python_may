from distutils.log import debug
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "Any string you want"


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/handle_data", methods=['POST'])
def handle_data():
    print(request.form)
    session['user_data'] = request.form['key']
    session['user_id'] = request.form['id']
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)