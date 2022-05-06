from flask import Flask, render_template
## ! import the Flask class from the flask module
app = Flask(__name__)  
## ! creating an instance of the Flask class and assignming it to the app variable  

## ! decorator that handles traffic for a given endpoint
@app.route('/hello')        
def hello_world():
    return 'Hello World!'

@app.route('/')
def index():
    return render_template('index.html')


## ! route for the '/about' endpoint 
@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)



## ! conditional stmt to make sure server.py is run from the terminal
if __name__=="__main__":    
    app.run(debug=True)    
# ! if it is, the run method belonging to the app object is called.
