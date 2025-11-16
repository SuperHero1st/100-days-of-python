from turtle import Turtle, Screen
import random
super = Turtle()

### Drawing a square ###

screen = Screen()
screen.colormode(255)

for i in range(3,11):
    random_color_1 = random.randint(0,255)
    random_color_2 = random.randint(0,255)
    random_color_3 = random.randint(0,255)
    super.color((random_color_1, random_color_2, random_color_3))  

    for x in range(i):
        super.forward(100)
        angle = 360 / i
        super.right(angle)













screen.exitonclick()
