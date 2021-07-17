from turtle import Turtle


class Score(Turtle):
    def __init__(self, position, score_1, score_2):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score1 = score_1
        self.score2 = score_2
        self.goto(position)

    def displaying_and_updating_score(self):
        # self.color("red")
        self.write(f"{self.score1} : {self.score2}", False, "center", ("Arial", 20, "bold"))

    def score_title(self):
        self.write("Score", True, "center", ("Arial", 20, "bold"))

    def updating_score(self, ball, paddle_right, paddle_left):
        ball.reset()
        paddle_right.reset()
        paddle_left.reset()
        self.reset()
        self.displaying_and_updating_score()

    def final_score(self):
        self.write(f"FINAL SCORE \n\n        {self.score1} : {self.score2}", False, "center", ("Arial", 20, "bold"))
