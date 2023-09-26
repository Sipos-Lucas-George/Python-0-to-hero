"""
    Pomodoro App, Work Timer (25/5){3}/25/20 and repeat
"""
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(str(timer))
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
    check_mark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        timer_label.config(text="WORK", fg=GREEN)
    elif reps % 8 != 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="BREAK", fg=RED)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    canvas.itemconfig(timer_text, text=f"{count // 60 if count // 60 > 9 else '0' + str(count // 60)}:"
                                       f"{count % 60 if count % 60 > 9 else '0' + str(count % 60)}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_mark_label.config(text=CHECK_MARK * (reps // 2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=0, column=1)
start_button = Button(text="Start", bg=YELLOW, activebackground=GREEN, fg=PINK, activeforeground=PINK,
                      highlightthickness=0, borderwidth=0, font=(FONT_NAME, 20, "bold"), command=start_timer)
start_button.grid(row=3, column=0)
reset_button = Button(text="Reset", bg=YELLOW, activebackground=GREEN, fg=PINK, activeforeground=PINK,
                      highlightthickness=0, borderwidth=0, font=(FONT_NAME, 20, "bold"), command=reset_timer)
reset_button.grid(row=3, column=3)
check_mark_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
check_mark_label.grid(row=4, column=1)

window.mainloop()
