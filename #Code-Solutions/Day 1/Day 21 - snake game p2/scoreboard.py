from turtle import Turtle
FONT = ("Courier", 16, "bold")
FONT2 = ("Arial", 28, "bold")

class Scoreboard(Turtle):

    def __init__(self, score = 0):
        super().__init__()
        self.score= score
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(0 , 270)
        self.write(f"Score = {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT2)



## could've used self.clear()



