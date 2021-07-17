from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
            "<p>This is a paragraph.</p>" \
            "<img src='https://media.giphy.com/media/rzJfhKZndpQME/giphy.gif'>"
            
def make_bold(func):
    def wrapper_function():
        return "<b>" + func() + "</b>"
    return wrapper_function   

def make_emphasis(func):
    def wrapper_function():
        return "<em>" + func() + "</em>"
    return wrapper_function   
    
def make_underline(func):
    def wrapper_function():
        return "<u>" + func() + "</u>"
    return wrapper_function    

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name.upper()}, you are {number} years old"

if __name__ == "__main__":
    app.run(debug=True)