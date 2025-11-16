from turtle import Turtle, Screen
import random,time


class Ball(Turtle):
    def __init__(self):     # Constructor Function, intialization
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move_distance = 10
        self.y_move_distance = 10

    def move(self):

        new_x = self.xcor() + self.x_move_distance
        new_y = self.ycor() + self.y_move_distance
        self.goto(new_x, new_y)
    
    
    def bounce_y(self):
            self.y_move_distance *= -1


    def bounce_x(self):
            self.x_move_distance *= -1.1

    def reset_ball(self, winner):
        self.goto(0,0)
        if winner =="left":
            self.x_move_distance= -10
            self.y_move_distance= -10
        elif winner =="right":
             self.y_move_distance =10
             self.x_move_distance =10
        


