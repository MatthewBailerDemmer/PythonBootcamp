MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def check_resources(option):
    water_left = resources["water"] - MENU[option]["ingredients"]["water"]
    milk_left = resources["milk"] - MENU[option]["ingredients"]["milk"]
    coffe_left = resources["milk"] - MENU[option]["ingredients"]["milk"]
    if water_left < 0:
        return "water"
    elif milk_left < 0:
        return "milk"
    elif coffe_left < 0:
        return "coffe"
    return ""


def money_transaction(option):
    pennies = int(input("How many pennies? "))
    nickels = int(input("How many nickels? "))
    dimes = int(input("How many dimes? "))
    quarters = int(input("How many quarters? "))
    total = pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25
    return total - MENU[option]["cost"]


def manage_resources(option):
    resources["water"] -= MENU[option]["ingredients"]["water"]
    resources["milk"] -= MENU[option]["ingredients"]["milk"]
    resources["coffee"] -= MENU[option]["ingredients"]["coffee"]
    resources["money"] += MENU[option]["cost"]


powerUp = True
while powerUp:
    answer = input("What coffe do you want to order?(espresso/latte/cappuccino)")
    if answer == "latte" or answer == "espresso" or answer == "cappuccino":
        isThereResources = check_resources(answer)
        if isThereResources == "":
            change = money_transaction(answer)
            if change > 0:
                manage_resources(answer)
                print(f"Here is your {answer}, your change was {round(change, 2)}")
            elif change == 0:
                manage_resources(answer)
                print(f"Here is your {answer}")
            else:
                print(f"There was not enough money to order a {answer}, money refunded")
        else:
            print(f"Not enough {isThereResources} to do it")
    elif answer == "report":
        print("Coffe Machine Resources:")
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffe: {resources['coffee']}")
        print(f"Money: {resources['money']}")
    elif answer == "getout":
        powerUp = False
        print("Thanks for ordering")
    else:
        print("Command not found")
