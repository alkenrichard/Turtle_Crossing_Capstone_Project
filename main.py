from turtle import Screen, Turtle
from turtle_user import TurtleUser
from car_segment import CarSegment
import time
from random import randint, choice
from cars import Cars
from level import Level

HEIGHT = 600
WIDTH = 600
SUM_OF_CAR = 15
COLOR = ['midnight blue', 'navy', 'royal blue', 'dodger blue', 'turquoise', 'light sea green', 'teal', 'aquamarine', 'sea green', 'dark green', 'sienna', 'maroon', 'crimson', 'dark magenta', 'dark orchid', 'blue violet', 'indigo', 'dark slate blue']

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title('Python Turtle Graphics')
screen.tracer(0)
screen.listen()

turtle = TurtleUser(HEIGHT)
cars = Cars(WIDTH, HEIGHT)
level = Level()
game_over = Turtle()

game_over.up()
game_over.ht()

for _ in range(SUM_OF_CAR):
    y_position = randint(int(-HEIGHT / 2 + 60), int(HEIGHT / 2 - 60))
    x_position = randint(int(-WIDTH / 2 + 60), int(WIDTH / 2 - 60))
    car_segment = CarSegment(WIDTH, (x_position + (WIDTH - 60) ,y_position), choice(COLOR))
    cars.add_card(car_segment)

game_is_on = True

screen.onkey(turtle.move, 'Up')
screen.onkey(turtle.move, 'w')

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for car in cars.cards:
        if car.distance(turtle) < 30:
            game_is_on = False

    cars.move_car()

    if turtle.ycor() >= HEIGHT / 2 - 20:
        level.increment_level()
        turtle.reset_position()
        cars.increment_speed(level.level)

game_over.write(arg="GAME OVER!!", align='center', font= ("Arial", 15, "normal"))

screen.exitonclick()
