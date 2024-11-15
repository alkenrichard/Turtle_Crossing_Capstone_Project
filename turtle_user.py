from turtle import Turtle

class TurtleUser(Turtle):
    def __init__(self, h):
        super().__init__()
        self.h = h
        self.up()
        self.shape('turtle')
        self.setheading(90)
        self.sety(-self.h / 2 + 20)

    def move(self):
        if self.ycor() < self.h / 2 - 20:
            self.sety(self.ycor() + 20)

    def reset_position(self):
        self.sety(-self.h / 2 + 20)
