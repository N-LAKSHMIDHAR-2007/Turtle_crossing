from turtle import Turtle
FONT = ("Algerian", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

    def scores(self):
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.clear()
        self.write(arg = f"Level:{self.level}", align = "left", font = FONT)


    def increase_score(self):
        self.level+=1

    def game_over(self):
        self.hideturtle()
        self.home()
        self.write(arg = "GAME OVER", align = "center", font = FONT)





