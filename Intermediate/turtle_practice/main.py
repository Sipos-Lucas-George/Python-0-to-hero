"""
    Turtle Package Drawing
"""
import turtle
from turtle import Turtle, Screen
from random import random, choice


my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("DeepSkyBlue")

# Square Shape
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)

# Dashed Line
# for _ in range(10):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

# Triangle, Square, Pentagon, Octagon, Hexagon, ..., Decagon
# for i in range(3, 11):
#     angle = 360 / i
#     my_turtle.pencolor((random(), random(), random()))
#     for _ in range(i):
#         my_turtle.forward(100)
#         my_turtle.left(angle)

# Random Path With Thicc Lines and speedy turtle
# my_turtle.speed(0)
# my_turtle.pensize(5)
# direction = [0, 90, 180, 270]
# for _ in range(300):
#     my_turtle.pencolor((random(), random(), random()))
#     my_turtle.setheading(choice(direction))
#     my_turtle.forward(20)

# Spirograph
# my_turtle.speed(0)
# my_turtle.hideturtle()
# number_of_circles = 100
# tilt = 360 / number_of_circles
# for i in range(number_of_circles):
#     my_turtle.pencolor((random(), random(), random()))
#     my_turtle.circle(100)
#     my_turtle.setheading(tilt*(i+1))

# Hirst Spot Painting
# turtle.colormode(255)
# my_turtle.speed(0)
# my_turtle.hideturtle()
# colors = colorgram.extract("img.png", 25)
# colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
# my_turtle.penup()
# start_point = -250
# my_turtle.goto(-250, start_point)
# for _ in range(12):
#     for _ in range(12):
#         my_turtle.dot(20, choice(colors))
#         my_turtle.forward(50)
#     start_point += 50
#     my_turtle.goto(-250, start_point)

screen = Screen()
screen.exitonclick()
