from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Pong Game")
screen.tracer(0)

lpaddle = Paddle((350, 0)) #Position of Paddle
rpaddle = Paddle((-350, 0)) #Position of Paddle


screen.listen()

screen.onkeypress(rpaddle.move_up, "w")
screen.onkeypress(rpaddle.move_down, "s")
screen.onkeypress(lpaddle.move_up, "Up")
screen.onkeypress(lpaddle.move_down, "Down")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280: #Limit of y axis of ball
        ball.bounce_y()

    if ball.distance(lpaddle) < 50 and ball.xcor() > 320 or ball.distance(rpaddle) < 50 and ball.xcor() < -320: #ball and paddle collision
        ball.bounce_x()

    if ball.xcor() > 380: #Limit of X axis of ball
        ball.ball_reset()
        scoreboard.l_point()

    if ball.xcor() < -380: #Limit of x axis of ball
        ball.ball_reset()
        scoreboard.r_point()


screen.exitonclick()