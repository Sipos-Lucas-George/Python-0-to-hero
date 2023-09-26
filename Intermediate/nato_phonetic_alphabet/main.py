"""
    Generates NATO Phonetic Alphabet as csv
"""
import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter: row.code for index, row in data.iterrows()}

while True:
    try:
        word = input("Enter a word: ").upper()
        print([phonetic_alphabet[x] for x in word])
        break
    except KeyError as error:
        print(f"Sorry {error} is not a letter")
