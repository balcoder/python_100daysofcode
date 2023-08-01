''' A representation of a Coffee Machine and its functions '''

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    "water": 2000,
    "milk": 1000,
    "coffee": 500,
    "money" : 0,
}


def get_report():
    '''Gets a report of all machine resources'''
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_drink_resources(drink):
    '''Check if enough resources for type of drink. Return boolean'''
    good_enough = True
    for ingredient in MENU[drink]["ingredients"]:
        resource = MENU[drink]["ingredients"][ingredient]
        if resource > resources[ingredient]:
            good_enough = False
            print(f"Sorry there is not enough {ingredient}")
    return good_enough

def process_coins(drink):
    '''Asks user to insert coins by type and returns amount inserted'''
    cost_of_drink = MENU[drink]["cost"]
    print(f"Please insert ${cost_of_drink} in coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    pennies = int(input("How many pennies: "))
    total = quarters * 0.25 + dimes * 0.10 + nickel * 0.05 + pennies * 0.01
    return total

def transaction_successful(total, drink):
    '''Check user has inserted enough money. If not print Sorry to screen.
    If too much give change and add cost to profit. Return true if enough
    money'''
    cost_of_drink = MENU[drink]["cost"]
    if total < cost_of_drink:
        print(f"Sorry that's not enough money. Money refunded: {total}")
        return False
    if total >= cost_of_drink:
        refund = total - cost_of_drink
        resources["money"] += total - refund
        if refund > 0:
            print(f"Here is ${round(refund, 2)} dollars in change.")
        return True
    return False

def make_coffee(drink):
    '''Check for resources, money given and makes coffee then updates
    the resources'''
    if check_drink_resources(drink):
        total = process_coins(drink)
        if transaction_successful(total, drink):
            for ingredient in MENU[drink]["ingredients"]:
                quantity = MENU[drink]["ingredients"][ingredient]
                resources[ingredient] -= quantity
            print(f"Here is your {drink}, Enjoy!")

def run_machine():
    '''Runs coffee machine untill off is entered'''
    keep_serving = True

    while keep_serving:
        action = input("What would you like? (espresso/latte/cappuccino): ")
        if action == "report":
            get_report()
        elif action == "off":
            keep_serving = False
            print("Machine going into maintenance mode. Bye")
            return
        elif action in MENU:
            make_coffee(action)
            # print(get_report())
        else:
            print("Wrong action. Actions are drinks (espresso/latte/cappuccino) or report")

run_machine()
