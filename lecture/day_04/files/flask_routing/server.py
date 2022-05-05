from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')        
def hello_world():
    return 'Hello World!'

@app.route("/dojo")
def about():
    return '<h1>Dojo</h1>'

@app.route('/say/<name>')
def say(name):
    return f"Hi {name.capitalize()}!"

@app.route('/<int:num>/<name>')
def repeat(num, name):
        return f"{name * num}"


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

