from turtle import Turtle
FONT = ("Courier", 8, "bold")
FONT2 = ("Arial", 28, "bold")

class Writer(Turtle):

    def __init__(self, ):
        super().__init__()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="left", font=FONT2)

    def write_text(self, position, content):
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(position)
        self.write(content, align= "center", font =FONT )


## could've used self.clear()



