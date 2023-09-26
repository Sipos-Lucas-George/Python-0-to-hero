"""
    Coffe machine 2.0 with OOP
"""
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
menu_item: MenuItem
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

cmd = input(f"What would you like {menu.get_items()}: ")
while cmd != "x":
    if cmd == "r":
        coffe_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(cmd)
        if menu_item is not None and coffe_maker.is_resource_sufficient(menu_item) \
                and money_machine.make_payment(menu_item.cost):
            coffe_maker.make_coffee(menu_item)
    cmd = input(f"What would you like {menu.get_items()}: ")
