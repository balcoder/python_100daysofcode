''' Representation of coffee machine using classes'''
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def run_coffer_machine():
    '''Runs the coffee machine until off is entered'''
    keep_serving = True
    options = menu.get_items()

    while keep_serving:
        action = input(f"What would you like? ({options}) ")
        if action == "report":
            coffee_maker.report()
            money_machine.report()
        elif action == "off":
            keep_serving = False
            print("Going into maintenance mode. Bye!")
            return
        elif action in menu.get_items():
            drink = menu.find_drink(action)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            print(f"Wrong action.Please select from {menu.get_items()} ")

run_coffer_machine()
