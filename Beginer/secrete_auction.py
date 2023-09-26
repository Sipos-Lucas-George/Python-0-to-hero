"""
    Secrete Auction
"""
import os

max_bid = 0
max_name = ""
while True:
    name = input("What's your name: ")
    bid = int(input("What's you bid: $"))
    if max_bid < bid:
        max_bid = bid
        max_name = name
    new_bidder = input("Is there another bidder(y/n): ")
    os.system("clear")
    if new_bidder == "n":
        break
print(f"The winner of this bidding round is {max_name} with ${max_bid}!")
