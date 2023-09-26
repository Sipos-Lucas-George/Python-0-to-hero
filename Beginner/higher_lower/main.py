"""
    Higher or lower
"""
import os
from data import data
from random import randint


def different_random_number() -> int:
    global first_data
    new_number = randint(0, len(data) - 1)
    while new_number == first_data:
        new_number = randint(0, len(data) - 1)
    return new_number


def translate_data(position: int) -> str:
    result = ""
    for x in data[position].values():
        result += x + ", " if isinstance(x, str) else str(x) + "M, "
    return result[:-2] + "."


def translate_data_secrete(position: int) -> str:
    result = ""
    for x in data[position].values():
        result += x + ", " if isinstance(x, str) else ""
    return result[:-2] + "."


cmd = input("Wanna play the game(y/n): ")
while cmd == "y":
    score = 0
    guessed = True
    first_data = randint(0, len(data) - 1)
    second_data = different_random_number()
    while True:
        os.system("clear")
        print(f"Your score is: {score}")
        print("A: " + translate_data(first_data))
        print("-" * 60)
        print("B: " + translate_data_secrete(second_data))
        guess = input("Who has more followers (A/B): ").lower()
        if (data[first_data]["follower_count"] > data[second_data]["follower_count"] and guess == "a") or \
                (data[first_data]["follower_count"] < data[second_data]["follower_count"] and guess == "b"):
            score += 1
            first_data = second_data
            second_data = different_random_number()
        else:
            break
    print(f"Congratulation! Your final score is: {score}")
    cmd = input("\nWanna play the game(y/n): ")
