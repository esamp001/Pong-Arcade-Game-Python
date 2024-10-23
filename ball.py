import turtle
from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        x = self.xcor() + self.x_move #move ball to x coordinate with speed of +10
        y = self.ycor() + self.y_move #move ball to y coordinate with speed of +10
        self.goto(x, y)  # move to ball to x and y coordinate

    def bounce(self):
        self.y_move *= -1







