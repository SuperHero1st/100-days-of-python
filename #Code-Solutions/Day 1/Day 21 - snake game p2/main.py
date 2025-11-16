from turtle import Turtle, Screen
import random,time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

#steup screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Super Snake Game")
screen.tracer(0)

score = 0

#Game loop
game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
        
    screen.update()
    time.sleep(0.06)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score +=1
        scoreboard.reset()
        scoreboard = Scoreboard(score)

    #Detect collision with wall
    if (snake.head.xcor() > 290) or (snake.head.xcor() < -290) or (snake.head.ycor() < -290) or (snake.head.ycor() > 290):
        scoreboard.game_over()
        game_is_on = False

    #Detect collision with tail
    for segment in snake.snake_pieces[3:]:
        if snake.head.distance(segment)< 20:
            game_is_on = False
            scoreboard.game_over()
            




screen.exitonclick()
