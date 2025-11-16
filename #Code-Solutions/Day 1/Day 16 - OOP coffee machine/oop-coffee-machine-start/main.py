from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_menu = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        machine.report()
        money_machine.report()
    elif user_input in machine_menu.get_items():
        drink = machine_menu.find_drink(user_input)
        sufficient_resources = machine.is_resource_sufficient(drink)
        if sufficient_resources:
            payment_successful = money_machine.make_payment(drink.cost)
            if payment_successful:
                    machine.make_coffee(drink)
    else:
        print("Invalid input. Please choose from (espresso/latte/cappuccino).")

    