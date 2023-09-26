import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.__cars: list[Turtle] = []
        self.__car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.__cars.append(new_car)

    def move_cars(self):
        for car in self.__cars:
            car.backward(self.__car_speed)

    def level_up(self):
        self.__car_speed += MOVE_INCREMENT

    def get_cars(self):
        return self.__cars
