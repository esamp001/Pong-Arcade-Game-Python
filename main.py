from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Pong Game")

paddle = Paddle()


screen.exitonclick()