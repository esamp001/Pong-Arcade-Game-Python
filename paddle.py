from turtle import Turtle



class Paddle:
    def __init__(self):
        self.save_all_segments = []
        self.create_paddle()

    def create_paddle(self, position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(x=0, y=0)
        self.save_all_segments.append(segment)

    def extend(self):
        self.create_paddle(self.save_all_segments[-1].position())



