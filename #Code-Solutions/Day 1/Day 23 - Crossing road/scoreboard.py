from turtle import Turtle
FONT = ("Courier", 16, "bold")
FONT2 = ("Arial", 28, "bold")

class Scoreboard(Turtle):

    def __init__(self, ):
        super().__init__()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT2)

    def update(self,level=1):
        self.clear()
        self.shape("square")
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(-230 , 270)
        self.write(f"Level: {level}", align="center", font=FONT)


## could've used self.clear()



