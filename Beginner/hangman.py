"""
    Hangman
"""
import random
import os


words = ["asset", "desire", "sniff", "resignation", "opera", "triangle", "potential", "pasture", "laser", "baseball"]
word = random.choice(words)
lives = 6
guesses = "".join(['_' for x in word])
print(guesses)
while lives > 0 and guesses.find('_') != -1:
    guess = input(f"Number of lives: {lives} - Take a guess: ")
    guessed = False
    for i, x in enumerate(word):
        if x == guess:
            guesses = guesses[:i] + x + guesses[i+1:]
            guessed = True
    if not guessed:
        lives -= 1
    os.system("clear")
    print(guesses, end="\n\n")
os.system("clear")
if lives == 0:
    print(f"You Lost! The word was {word}")
else:
    print(f"You Won! The word was - {word} -")
