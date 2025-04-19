from turtle import Turtle


ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.teleport(x=0,y=0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
