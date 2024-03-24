from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(r_paddle) < 30 and ball.xcor() > 330 or ball.distance(l_paddle) < 30 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        score_board.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        score_board.r_point()






screen.exitonclick()

