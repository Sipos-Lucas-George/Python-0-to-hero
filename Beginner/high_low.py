"""
    High or Low
"""
import os
from random import randint


cmd = input("Wanna play (y/n): ")
while cmd == "y":
    os.system("clear")
    number_to_guess = randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    attempts = int(input("Write the number of attempts you want to have: "))
    while attempts != 0:
        guess = int(input("Take a guess: "))
        if guess == number_to_guess:
            print(f"You guessed it! The number was {number_to_guess}")
            break
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Too low!")
        attempts -= 1
    else:
        print(f"You are out of attempts! The number was {number_to_guess}")
    cmd = input("Wanna play (y/n): ")

