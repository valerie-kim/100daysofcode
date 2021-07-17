from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

number = random.randint(0,9)       

@app.route("/<int:num>")
def guess(num):
    if num == number:
        return "<h1 style='text-align: center'>You got it! Congrats!</h1>"\
                "<img src='https://media.giphy.com/media/l2YWCPLrCIaNc9QT6/giphy.gif'>"
    elif number < num <= number+2: 
        return "<h1 style='text-align: center'>Slightly high</h1>"\
                "<img src='https://media.giphy.com/media/rhC8duvjyYNhRxMBbQ/giphy.gif'>"
    elif  number > num >= number-2: 
        return "<h1 style='text-align: center'>Slightly low</h1>"\
                "<img src='https://media.giphy.com/media/SsHZjFZTqLLqTedLw9/giphy.gif>"
    elif number+2 < num:
        return "<h1 style='text-align: center'>Too high</h1>"\
                "<img src='https://media.giphy.com/media/2cei8MJiL2OWga5XoC/giphy.gif'>"
    elif number-2 > num:
        return "<h1 style='text-align: center'>Too low</h1>"\
                "<img src='https://media.giphy.com/media/3o6Zt6qld6hkPkP0C4/giphy.gif'>"    
    else:
        return "<h1 style='text-align: center'>Please enter a number between 0 and 9</h1>"\
                "<img src='https://media.giphy.com/media/Yycc82XEuWDaLLi2GV/giphy.gif'>"
            
if __name__ == "__main__":
    app.run(debug=True)
    
