"""
    Turtle Package && Pretty Table Package
"""
from turtle import Turtle, Screen


my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("DeepSkyBlue")
my_turtle.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
