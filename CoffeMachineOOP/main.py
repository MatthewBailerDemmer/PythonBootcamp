from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

powerUp = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while powerUp:

    order = input(f"What would you like to order? ({menu.get_items()}) ")
    if order != "cappuccino" and order != "latte" and order != "espresso":
        if order == "report":
            coffee_maker.report()
            money_machine.report()
        elif order == "power down":
            print("Thanks for ordering")
            powerUp = False
        else:
            print("Command not found")
    else:
        item = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)
