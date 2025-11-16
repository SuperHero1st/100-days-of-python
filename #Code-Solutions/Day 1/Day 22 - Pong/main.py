from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


game_is_on = True
paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

left_score = 0
right_score = 0
left_scoreboard = Scoreboard(position = (-90 ,200))
right_scoreboard = Scoreboard(position = (90 ,200))

screen.listen()
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


while game_is_on: 
    screen.update()
    time.sleep(0.1)
    ball.move()
    
    ## Detect collision with top and bottom walls:
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    ## Detect collision with paddles:
    if (ball.distance(paddle) <50 and ball.xcor() >320) or (ball.distance(left_paddle) < 50 and ball.xcor() <-320):
        ball.bounce_x() 
    
    ## Detect collision with right,left walls:
    if (ball.distance(paddle) >50 and ball.xcor() >380):    ## left player scores
        ball.reset_ball(winner="left")
        left_score +=1
        left_scoreboard.update(left_score)

    if (ball.distance(left_paddle) > 50 and ball.xcor() <-380):
        ball.reset_ball(winner="right")
        right_score +=1
        right_scoreboard.update(right_score)
