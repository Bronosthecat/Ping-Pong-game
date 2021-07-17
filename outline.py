from turtle import Turtle


class Decorate(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.pensize(2)
        self.hideturtle()
        self.penup()
        self.goto(-590, -345)
        self.pendown()
        self.setheading(90)
        self.goto(590, -345)
        self.goto(590, 345)
        self.goto(-590, 345)
        self.goto(-590, -345)
