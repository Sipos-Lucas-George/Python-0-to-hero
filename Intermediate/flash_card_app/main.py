"""
    Flash Card App Teaching Italian/French
"""
from tkinter import *
from random import choice
from pandas import *

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("./data/italian_english.csv")
data = data.to_dict(orient="records")
current_card = {}
flipped = 0


def format_word():
    global current_card
    new_word = current_card['Italian'].split('/')
    if len(new_word) == 3:
        return new_word[0] + '\n' + new_word[1] + "/" + new_word[2]
    return new_word[0] + '\n' + new_word[1]


def get_random_word():
    global current_card
    current_card = choice(data)
    new_word = current_card['Italian'].split('/')
    if len(new_word) == 3:
        return new_word[0] + '\n' + new_word[1] + "/" + new_word[2]
    return new_word[0] + '\n' + new_word[1]


def next_card():
    global flipped
    flipped = 0
    canvas.itemconfig(language, text="Italian", fill="black")
    canvas.itemconfig(word, text=get_random_word(), fill="black")
    canvas.itemconfig(card, image=card_front_image)


def is_known():
    data.remove(current_card)
    new_data = DataFrame(data)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def flip_card(_):
    global flipped
    if flipped == 0:
        canvas.itemconfig(language, text="English", fill="white")
        canvas.itemconfig(word, text=current_card["English"], fill="white")
        canvas.itemconfig(card, image=card_back_image)
        flipped = 1
    else:
        canvas.itemconfig(language, text="Italian", fill="black")
        canvas.itemconfig(word, text=format_word(), fill="black")
        canvas.itemconfig(card, image=card_front_image)
        flipped = 0


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.bind("<Return>", flip_card)
# window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_image)
language = canvas.create_text(400, 150, text="Italian", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 300, text=get_random_word(), font=("Ariel", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                      fg=BACKGROUND_COLOR, activeforeground=BACKGROUND_COLOR,
                      highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                      fg=BACKGROUND_COLOR, activeforeground=BACKGROUND_COLOR,
                      highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)

window.mainloop()
