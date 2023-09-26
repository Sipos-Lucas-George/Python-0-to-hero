"""
    Password Manager For Websites
"""
import pyperclip
import json
from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox

FONT = ("Courier", 16, "")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any of the fields empty!")
        return
    data = {}
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
    except FileNotFoundError:
        data = new_data
        pass
    finally:
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave search field empty!")
        return
    data = {}
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        messagebox.showinfo(title="Error", message=f"Email: {data[website]['email']}\n"
                                                   f"Password: {data[website]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found!")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for the website exists!")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
search_button = Button(text="Search", width=7, command=find_password)
search_button.grid(row=1, column=2)
website_entry.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
email_username_entry = Entry(width=36)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(END, "lucas.sipos.george@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)
password_button = Button(text="Generate", width=7, command=generate_password)
password_button.grid(row=3, column=2)

save_button = Button(text="Save", width=33, command=save)
save_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
