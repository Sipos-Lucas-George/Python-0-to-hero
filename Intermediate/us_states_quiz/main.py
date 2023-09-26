"""
    U.S. States Game using turtle and pandas
"""
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
data = pandas.read_csv("50_states.csv")
while len(guessed_states) < 51:
    answer_state = screen.textinput(F"{len(guessed_states)}/50 States Correct", "What's another state's name?").title()
    coordinates = data[data["state"] == answer_state]

    if answer_state == "Exit":
        break

    if len(coordinates) != 0 and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(int(coordinates.x.item()), int(coordinates.y.item()))
        new_turtle.write(answer_state)

dictionary_with_states_to_learn = {"States": data[~data.state.isin(guessed_states)].state.to_list()}
data_frame = pandas.DataFrame(dictionary_with_states_to_learn)
data_frame.to_csv("states_to_learn.csv")
