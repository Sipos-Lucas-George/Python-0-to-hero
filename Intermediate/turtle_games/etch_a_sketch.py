"""
    Etch-A-Sketch App
"""
from turtle import Turtle, Screen


def move_forward():
    my_turtle.forward(10)


def move_back():
    my_turtle.back(10)


def turn_left():
    global angle
    angle += 10
    my_turtle.setheading(angle)


def turn_right():
    global angle
    angle -= 10
    my_turtle.setheading(angle)


my_turtle = Turtle()
screen = Screen()
angle = 0
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=my_turtle.reset)

screen.exitonclick()
