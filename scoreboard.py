from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 0

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 18))

    def level_up(self):
        self.level += 1
        self.goto(-280, 280)
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=("Arial", 18))