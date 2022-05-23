from flask import Flask, jsonify, render_template
from app import data

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(data)

@app.route('/skywalker')
def skywalker():
    return render_template('index.html', data = data)


if __name__ == "__main__":
    app.run(debug = True)