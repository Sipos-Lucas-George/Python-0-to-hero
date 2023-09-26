"""
    Password generator
"""
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Password Generator!")
nr_letters = int(input("Number of letters: "))
nr_numbers = int(input("Number of numbers: "))
nr_symbols = int(input("Number of symbols: "))

password_list = []
for x in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for x in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
for x in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password = ""
for x in password_list:
    password += x
print(password)
