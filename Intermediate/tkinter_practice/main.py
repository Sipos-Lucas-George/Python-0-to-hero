"""
    GUI with tkinter
"""
import tkinter


def button_clicked():
    count_label["text"] = f"{int(count_label['text']) + 1}"
    my_label["text"] = input_field.get() if len(input_field.get()) > 0 else "I Am a Label"


window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="I Am a Label", font=("Courier", 24))
my_label.pack()
# my_label.pack(expand=True)

# my_label["text"] = "New Text"
# my_label.config(text="New Text")

count_label = tkinter.Label(text="0", font=("Courier", 24))
count_label.pack()

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()
button.config(padx=20, pady=20)

input_field = tkinter.Entry(width=10)
input_field.place(x=10, y=3)

# Grid view
# label1 = tkinter.Label(text="C0R0", font=("Courier", 12))
# label1.grid(column=0, row=0)
# label2 = tkinter.Label(text="C1R1", font=("Courier", 12))
# label2.grid(column=1, row=1)
# label3 = tkinter.Label(text="C2R2", font=("Courier", 12))
# label3.grid(column=2, row=2)

window.mainloop()
