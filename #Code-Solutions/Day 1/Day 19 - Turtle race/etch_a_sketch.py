from turtle import Turtle, Screen

super = Turtle()
screen = Screen()
super.shape("turtle")

def move_forward():
    super.forward(10)
    print(super.heading())


def move_backward():
    super.back(10)


def rotate_counter_clockwise():
    new_heading = super.heading() + 10
    super.setheading(new_heading)


def rotate_clockwise():
    new_heading = super.heading() + 10
    super.setheading(new_heading)


def reset():
    screen.resetscreen()


def reset_2():
    super.clear()
    super.penup()
    super.home()
    super.pendown()


screen.listen()
screen.onkey(move_forward, key ="w")     
screen.onkey(move_backward, key ="s")   
screen.onkey(rotate_counter_clockwise, key ="a")     
screen.onkey(rotate_clockwise, key ="d")
screen.onkey(reset, key="c")



screen.exitonclick()