from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def move_up(self):
        y = self.ycor()
        self.sety(y + 20)

    def move_down(self):
        y = self.ycor()
        self.sety(y - 20)

