from turtle import Turtle

class CarSegment(Turtle):
    def __init__(self, w, position, color):
        super().__init__()
        self.level = 1
        self.w = w
        self.color(color)
        self.up()
        self.shape('square')
        self.speed(9)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(position)


