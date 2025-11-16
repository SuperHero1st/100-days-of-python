import turtle as t
import random

super = t.Turtle()
t.colormode(255)

super.pensize(1)
super.speed(0)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)


angles=[0, 90, 180 ,270]
loops = 120
for i in range(loops):

    super.setheading(360/loops*i)
    super.color(random_color())
    super.circle(100)




screen = t.Screen()
screen.exitonclick()










