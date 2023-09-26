"""
    Mile To Kilometer Converter
"""
from tkinter import *


def convert_miles_to_km():
    kilometer_result["text"] = round(float(miles_input.get())*1.609, 2)


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)
miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)
kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
