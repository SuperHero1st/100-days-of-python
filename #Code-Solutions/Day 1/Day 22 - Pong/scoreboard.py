from turtle import Turtle
FONT = ("Courier", 70, "bold")
FONT2 = ("Arial", 28, "bold")

class Scoreboard(Turtle):

    def __init__(self, score = 0, position = (0,250)):
        super().__init__()
        self.score= score
        self.hideturtle()
        self.position = position
        self.color("white")
        self.penup()
        self.goto(position)
        self.write(f"{self.score}", align="center", font=FONT)

    def update(self,score):
        self.clear()
        self.score = score
        self.write(f"{self.score}", align="center", font=FONT)
        self.goto(self.position)


## could've used self.clear()



