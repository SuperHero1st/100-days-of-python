from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = "Make your bet ", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = 100
is_race_on = False
turtles = {}

for color in colors:
    turtles[color] = Turtle(shape = "turtle") 
    current_turtle = turtles[str(color)]
    current_turtle.color(str(color))
    current_turtle.penup()
    current_turtle.goto(x= -230, y= y_position)
    y_position -= 30


if user_bet:
    is_race_on = True

while is_race_on:
    for color in colors:
        random_distance = random.randint(0,10)

        # if str(color) == "red":
        #     random_distance= (10)         # Checking the winning condition
        
        current_turtle = turtles[str(color)]
        current_turtle.forward(random_distance)

        if current_turtle.xcor() >= 230:
            is_race_on = False
            winning_color = current_turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()