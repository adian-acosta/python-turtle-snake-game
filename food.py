import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.refresh()

    def refresh(self):
        # Ensures the food will always be in the snake's path
        # TODO find a way to have this but for it to adjust to the snake's move distance, hate having hard coded numbers
        random_x = random.randint(-280 // 20, 280 // 20) * 20
        random_y = random.randint(-280 // 20, 260 // 20) * 20
        self.teleport(random_x, random_y)
