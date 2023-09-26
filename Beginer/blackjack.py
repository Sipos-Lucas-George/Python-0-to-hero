"""
    Blackjack
"""
import os
from random import randint, shuffle
from time import sleep


def verify_deck():
    global deck
    value = min(deck, key=lambda k: k[2])
    if value[2] == 0:
        deck.remove(value)


def deal_cards():
    global card_usage
    global player_cards
    global computer_cards
    global player_score
    global computer_score
    for _ in range(2):
        card = randint(0, len(deck) - 1)
        deck[card][2] -= 1
        player_score += deck[card][1]
        player_cards.append(deck[card][0])
    for _ in range(2):
        card = randint(0, len(deck) - 1)
        deck[card][2] -= 1
        computer_score += deck[card][1]
        computer_cards.append(deck[card][0])
    verify_deck()


def recalculate_score(cards: list) -> int:
    score = 0
    number_of_aces = 0
    deck_values = {"A": 11, "X": 10, "J": 10, "Q": 10, "K": 10}
    for x in cards:
        score += deck_values.get(x, ord(x) - ord("0"))
        if x == "A":
            number_of_aces += 1
    while number_of_aces != 0 and score > 21:
        number_of_aces -= 1
        score -= 10
    return score


def give_card(entity: list, score: int):
    card = randint(0, len(deck) - 1)
    deck[card][2] -= 1
    score += deck[card][1]
    entity.append(deck[card][0])
    verify_deck()


def game_decider() -> int:
    global player_score
    global player_cards
    global computer_score
    global computer_cards
    if computer_score != player_score:
        return 1 if player_score > computer_score else -1
    if len(computer_cards) != len(player_cards):
        return 1 if len(player_cards) > len(computer_cards) else -1
    if computer_cards[1] == computer_cards[2] == "A" == player_cards[1] == player_cards[2]:
        return 0
    if computer_cards[1] == computer_cards[2] == "A":
        return -1
    if player_cards[1] == player_cards[2] == "A":
        return 1
    return 0


cmd = input("Wanna play blackjack (y/n): ")
os.system("clear")
while cmd == "y":
    player_cards = []
    computer_cards = []
    player_score = 0
    computer_score = 0
    card_usage = {}
    game_winner = True
    deck = [["A", 11, 4], ["2", 2, 4], ["3", 3, 4], ["4", 4, 4], ["5", 5, 4], ["6", 6, 4], ["7", 7, 4], ["8", 8, 4],
            ["9", 9, 4], ["X", 10, 4], ["J", 10, 4], ["Q", 10, 4], ["K", 10, 4]]
    shuffle(deck)
    deal_cards()
    print("Player cards:", *player_cards, f"  Score: {player_score}")
    print(f"Dealer cards: {computer_cards[0]}   Score: {recalculate_score(computer_cards[:-1])}")

    player_choice = input("Hit (y/n): ")
    while player_choice == "y":
        give_card(player_cards, player_score)
        player_score = recalculate_score(player_cards)
        print("Player cards:", *player_cards, f"  Score: {player_score}")
        if player_score > 21:
            game_winner = False
            break
        player_choice = input("Hit (y/n): ")

    print("Dealer cards:", *computer_cards, f"  Score: {computer_score}")
    if game_winner:
        while computer_score < 17:
            sleep(1)
            give_card(computer_cards, computer_score)
            computer_score = recalculate_score(computer_cards)
            print("Dealer cards:", *computer_cards, f"  Score: {computer_score}")
    final_decision = 0
    if game_winner:
        final_decision = game_decider()
    if not game_winner or final_decision == -1:
        print("You lost!")
    elif final_decision == 1:
        print("You won!")
    else:
        print("It's a draw!")
    print("Player cards:", *player_cards, f"  Score: {player_score}")
    print("Dealer cards:", *computer_cards, f"  Score: {computer_score}")
    cmd = input("Wanna play blackjack (y/n): ")
    os.system("clear")

