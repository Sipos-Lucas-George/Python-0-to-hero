"""
    Coffe machine
"""
from data import *


def report():
    result = ""
    for key, value in resources.items():
        result += key.title() + ": " + (str(value) + "ml" if key != "coffee" else str(value) + "g") + "\n"
    print(result[:-1])


def request_money() -> int:
    cents = 0
    print("Please insert coins!")
    cents += 50 * int(input("How many $0.50: "))
    cents += 10 * int(input("How many $0.10: "))
    cents += 5 * int(input("How many $0.05: "))
    cents += int(input("How many $0.01: "))
    return cents


def verify_resources(ingredients: {}) -> str:
    result = ""
    for key, value in resources.items():
        if value < ingredients[key]:
            result += key + ", "
    return result if len(result) == 0 else result[:-2]


def make_coffe(coffe: {}):
    global cmd
    global cmds
    resource = verify_resources(coffe["ingredients"])
    if len(resource) > 0:
        print(f"Sorry there is not enough {resource}!")
        return

    cents = request_money()/100
    coffe_cost = coffe["cost"]
    if cents < coffe_cost:
        print("Sorry that's not enough money. Money refunded!")
        return
    if cents > coffe_cost:
        print(f"Here is {cents - coffe_cost:.2f} in change")
    print(f"Here is your {cmds[cmd]}")
    for key, value in resources.items():
        resources[key] = value - coffe["ingredients"][key]


cmds = {
    "e": "espresso",
    "l": "latte",
    "c": "cappuccino",
}
cmd = input("What would you like (espresso, latte, cappuccino): ")
while cmd != "x":
    if cmd == "r":
        report()
    else:
        make_coffe(menu[cmds[cmd]])
    cmd = input("What would you like (espresso, latte, capuccino): ")
