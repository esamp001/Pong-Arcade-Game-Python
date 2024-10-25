import turtle
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pensize(20)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        x = self.xcor() + self.x_move #move ball to x coordinate with speed of +10
        y = self.ycor() + self.y_move #move ball to y coordinate with speed of +10
        self.goto(x, y)  # move to ball to x and y coordinate

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_x()









