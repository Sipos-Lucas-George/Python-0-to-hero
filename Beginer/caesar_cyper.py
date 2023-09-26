"""
    Caesar cyper
"""
def caesar(word, offset):
    new_word = ""
    for x in word:
        new_word += chr(ord(x) + offset)
    return new_word


cmd = input("Encode or decode(e/d/x): ")
while cmd != "x":
    word = input("Word: ")
    offset = int(input("Offset: "))
    offset = -offset if cmd == "d" else offset
    print(f"Result: {caesar(word, offset)}")
    cmd = input("Encode or decode(e/d/x): ")
print("Goodbye!")
