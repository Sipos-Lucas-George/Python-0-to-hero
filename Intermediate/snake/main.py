"""
    Snake Game
"""
from time import sleep
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()
    if snake.get_head().distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if abs(snake.get_head().xcor()) > 290 or abs(snake.get_head().ycor()) > 290:
        scoreboard.reset()
        snake.reset()

    if snake.collision_with_tail():
        scoreboard.reset()
        snake.reset()

screen.exitonclick()
