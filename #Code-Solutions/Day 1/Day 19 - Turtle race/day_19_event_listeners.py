from turtle import Turtle, Screen

super = Turtle()
screen = Screen()

def move_forward():
    super.forward(10)

screen.listen()
screen.onkey(move_forward, key ="space")     # When we pass a function, we don't include the parenthesis () at the end

screen.exitonclick()