from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_len=1, stretch_wid=1, outline=1.5)
        self.setheading(random.choice([10, 170, 350, 190]))
        self.speed("normal")

    def bouncing_from_side_walls(self):
        a = self.heading()
        self.setheading(360 - a)
        self.forward(60)

    def bouncing_from_paddle(self):
        a = self.heading()
        self.setheading(random.choice([(170 - a), (190 - a)]))
        self.forward(60)
