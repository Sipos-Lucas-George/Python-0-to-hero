"""
    Pong Game
"""
from turtle import Screen
from player import Player
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)

player_one = Player(350, 0)
player_two = Player(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.title("Pong")
screen.setup(800, 600)
screen.bgcolor("black")

screen.listen()
screen.onkey(key="Up", fun=player_one.up)
screen.onkey(key="Down", fun=player_one.down)
screen.onkey(key="w", fun=player_two.up)
screen.onkey(key="s", fun=player_two.down)

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    if ball.xcor() > 380:
        scoreboard.increase_player_two()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.increase_player_one()
        ball.reset_position()

    if (ball.distance(player_one) < 50 or ball.distance(player_two) < 50) and abs(ball.xcor()) > 320:
        ball.bounce_x()

screen.exitonclick()
