"""
    Turtle Race Game
"""
from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(1000, 800)
turtles = []
colors = ["red", "purple", "blue", "orange", "yellow"]
position = -100
for i in range(5):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].shapesize(2, 2)
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].speed(0)
    turtles[i].goto(-450, position + (i * 70))

user_bet = ""
while user_bet not in colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

still_racing = True
while still_racing:
    for x in turtles:
        x.forward(randint(0, 10))
        if x.xcor() > 500:
            still_racing = False

winner = max(turtles, key=lambda t: t.xcor()).color()[0]
screen.bye()
if winner == user_bet:
    print(f"You won! The {winner} turtle is the winner!")
else:
    print(f"You lost! The {winner} turtle is the winner!")
