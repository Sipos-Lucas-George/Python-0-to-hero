"""
    Mail Merge Invitation
"""
PLACE_HOLDER = "[name]"
text: str

with open("./Input/Letters/starting_letter.txt") as file:
    text = file.read()

with open("./Input/Names/invited_names.txt") as file:
    for name in file.read().split('\n'):
        new_text = text.replace(PLACE_HOLDER, name)
        with open(f"./Output/ReadyToSend/{name}.txt", "w") as file:
            file.write(new_text)
