from turtle import Turtle, Screen
import random
super = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "tomato"]

super.pensize(10)
super.speed(0)

angles=[0, 90, 180 ,270]
for i in range(1000):

    random_color = random.choice(colours)
    super.color(random_color)
    super.forward(20)
    angle = random.choice(angles)
    super.setheading(angle)




screen = Screen()
screen.exitonclick()










