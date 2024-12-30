FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setup()
        self.lvl = 1
        self.show_level()


    def setup(self):
        self.penup()
        self.hideturtle()
        self.goto(-250,250)

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.lvl}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT, align="center")

