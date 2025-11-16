from flask import Flask 

def make_bold(function):
    def wrapper_func():
        return "<b>" + function() + "</b>"
    return wrapper_func


def make_italic(function):
    def wrapper_func():
        return "<em>" + function() + "</em>"
    return wrapper_func


def make_underlined(function):
    def wrapper_func():
        return "<u>" + function() + "</u>"
    return wrapper_func


app = Flask(__name__)


@app.route("/")
@make_bold
@make_underlined
@make_italic
def hello_world():
    return "HELLO WORLD !!"

# def hello_world():
#     return "<h1 style = 'text-align: center'> Hello, World! </h1>" \
#            "<p> This is a paragraph. </p>" \
#            "<img src = 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWdrbHdyNjZvaWd4YnIzc2k4Ymx0dmR0aDgxM3FrNjZ1emh4bjV5eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YRVP7mapl24G6RNkwJ/giphy.webp' width=500>"

@app.route("/username/<name>/<int:number>")
def greet(name, number=0):
    return f"Hello there {name}, you are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
    