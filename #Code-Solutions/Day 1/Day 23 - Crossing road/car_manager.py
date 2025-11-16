from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
STARTING_X_COR = 320

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.move_increment = 10

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance ==6:
            rand_color = random.choice(COLORS)
            rand_y_cor = random.randint(-250,250)
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(rand_color)
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto((STARTING_X_COR, rand_y_cor))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.move_increment
            car.goto((new_x, car.ycor()))

    def update_speed(self):
        self.move_increment *= 1.2
