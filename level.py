from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.up()
        self.goto(-280, 270)
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align='left', font= ("Arial", 15, "normal"))

    def increment_level(self):
        self.level += 1
        self.update()
