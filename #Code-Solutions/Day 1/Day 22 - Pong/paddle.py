from turtle import Turtle, Screen
import random,time
MOVE_DISTANCE = 30

class Paddle(Turtle):

    def __init__(self, position):     # Constructor Function, intialization
        super().__init__()
        self.position = position
        self.create_paddle()


    def create_paddle(self):
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(self.position)
        self.shapesize(stretch_wid=5, stretch_len=1)


    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


