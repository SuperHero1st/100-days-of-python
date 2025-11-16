from turtle import Turtle, Screen
import random,time
MOVE_DISTANCE = 20

class Snake:

    def __init__(self, snake_length = 3):     # Constructor Function, intialization
        self.snake_length = snake_length
        self.snake_pieces = []
        self.create_snake()
        self.head = self.snake_pieces[0]


    def create_snake(self):
        x_pos = 0
        for i in range(self.snake_length):
            snake_piece = Turtle("square")
            snake_piece.penup()
            self.snake_pieces.append(snake_piece)
            snake_piece.color("white")
            snake_piece.goto(x= x_pos, y = 0)
            x_pos -= 20


    def move(self):
        for piece_num in range(self.snake_length-1 , 0, -1):
            current_piece = self.snake_pieces[piece_num]
            following_piece = self.snake_pieces[piece_num-1]
            current_piece.goto(following_piece.position())


        self.head.forward(MOVE_DISTANCE)
    

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)




    

