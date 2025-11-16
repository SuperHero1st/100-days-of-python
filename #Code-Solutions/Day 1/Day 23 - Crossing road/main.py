import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard= Scoreboard()
carmanager = CarManager()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
level = 1

while game_is_on:

    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_cars()

    # Detecting collision with cars
    for car in carmanager.all_cars:
        if car.distance(player) <= 20:
            game_is_on = False
            scoreboard.game_over()

    # Detecting being in finish line 
    if player.ycor()>= FINISH_LINE_Y:
        player.back_to_start()
        level+=1
        scoreboard.update(level)
        carmanager.update_speed()

screen.exitonclick()