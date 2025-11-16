from flask import Flask 
import random

app = Flask(__name__)

random_num = random.randint(1,9)

def make_bold_h1(function):
    def wrapper_func(*args, **kwargs):
        return "<h1><b>" +  function(*args, **kwargs) + "</h1></b>"
    return wrapper_func

@app.route("/")

def main():
    return "<h1>Guess a number between 0 and 9 </h1>" \
            "<img src= 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/URL/<int:number>")
@make_bold_h1
def check_num( number):
    global random_num
    if number > random_num:
        return "Too High, Try again <br><br>" \
            "<img src= 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjhzOGJ4NmJlY2ZrOWRzd2cwdmdxNGVpb3RpNzB4MDhwZWc5OTUweSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wHB67Zkr63UP7RWJsj/giphy.webp'>"
    elif number < random_num:
        return "Too low, Try again <br><br>" \
            "<img src= 'https://media4.giphy.com/media/PR3585ZZSvcHO9pa76/200.webp?cid=790b7611knrldkjrny9d2pt82a5m50c8ypgwppko3dz9z5j6&ep=v1_gifs_search&rid=200.webp&ct=g'>"
    else:
        return "You found me! <br><br>" \
            "<img src= 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3EwMDMxYXdjdndwY3oyMTBrcG13bWhxaTNlMWMzMnVranZhN3RzYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2Sq5GffrCyUMEXjW/giphy.webp'>"


if __name__ == "__main__":
    app.run(debug=True)
    