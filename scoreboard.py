from turtle import Turtle
FONT = ("Courier", 24, "normal")
AL = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 1

    def draw_level(self):
        self.goto(-200, 240)
        self.write(f"Level: {self.level}", False, align=AL, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, align=AL, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()