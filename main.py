from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Score
from outline import Decorate
import time


PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0
POSITIONS = ((0, 315), (0, 285), (0, 0))


screen = Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.tracer(0)
score_main = Score(POSITIONS[0], PLAYER_1_SCORE, PLAYER_2_SCORE)
score_main.color("red")
score_main.score_title()
a = Decorate()

time.sleep(1.5)

true_statement1 = True

while true_statement1:

    ball = Ball()
    paddle_right = Paddle((575, 0))
    paddle_left = Paddle((-580, 0))
    score2 = Score(POSITIONS[1], PLAYER_1_SCORE, PLAYER_2_SCORE)
    score2.displaying_and_updating_score()

    true_statement = True

    screen.listen()
    screen.onkey(paddle_right.move_up, "Up")
    screen.onkey(paddle_right.move_down, "Down")
    screen.onkey(paddle_left.move_up, "w")
    screen.onkey(paddle_left.move_down, "s")

    while true_statement:

        ball.forward(10)
        time.sleep(0.0008)
        screen.update()

        if paddle_right.distance(ball) <= 60.0:
            ball.bouncing_from_paddle()

        elif paddle_left.distance(ball) <= 60.0:
            ball.bouncing_from_paddle()

        elif ball.xcor() > 600:
            PLAYER_1_SCORE += 1
            score2.updating_score(ball, paddle_right, paddle_left)
            true_statement = False
            time.sleep(1)

        elif ball.xcor() < -600:
            PLAYER_2_SCORE += 1
            score2.updating_score(ball, paddle_right, paddle_left)
            true_statement = False
            time.sleep(1)

        if ball.ycor() >= 340 or ball.ycor() <= -340:
            ball.bouncing_from_side_walls()

        if PLAYER_1_SCORE == 10 or PLAYER_2_SCORE == 10:
            score_main.reset()
            final_score = Score(POSITIONS[2], PLAYER_1_SCORE, PLAYER_2_SCORE)
            final_score.color("red")
            final_score.final_score()
            true_statement1 = False


screen.exitonclick()
