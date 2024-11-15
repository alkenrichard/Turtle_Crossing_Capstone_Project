from random import randint

CAR_INCREMENT = 10

class Cars:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.cards = []

    def add_card(self, segment):
        self.cards.append(segment)

    def move_car(self):
        for seg in self.cards:
            if seg.xcor() > -self.width / 2 - 60:
                seg.setx(seg.xcor() - (CAR_INCREMENT * seg.level))
            else:
                y_position = randint(int(-self.height / 2 + 60), int(self.height / 2 - 60))
                x_position = randint(int(-self.width / 2 + 60), int(self.width / 2 - 60))
                seg.teleport(x_position + (self.width - 60), y_position)

    def increment_speed(self, speed):
        for seg in self.cards:
            seg.level = speed
