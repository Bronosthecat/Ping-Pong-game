from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("blue")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.speed("fastest")
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.goto(position)

    def move_up(self):
        if self.ycor() <= 265:
            self.forward(55)

    def move_down(self):
        if self.ycor() >= -265:
            self.backward(55)
