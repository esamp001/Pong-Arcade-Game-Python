from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Pong Game")
screen.tracer(0)

lpaddle = Paddle((350, 0))
rpaddle = Paddle((-350, 0))


screen.listen()
screen.onkey(rpaddle.move_up, "w")
screen.onkey(rpaddle.move_down, "s")
screen.onkey(lpaddle.move_up, "Up")
screen.onkey(lpaddle.move_down, "Down")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(lpaddle) < 50 and ball.xcor() > 340 or ball.distance(rpaddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_reset()

    if ball.xcor() < -380:
        ball.ball_reset()


screen.exitonclick()