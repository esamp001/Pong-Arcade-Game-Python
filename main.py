from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Pong Game")
screen.tracer(0)

lpaddle = Paddle((350, 0))
rpaddle = Paddle((-350, 0))

screen.listen()
screen.onkey(rpaddle.move_up, "Up")
screen.onkey(rpaddle.move_down, "Down")
screen.onkey(lpaddle.move_up, "w")
screen.onkey(lpaddle.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()