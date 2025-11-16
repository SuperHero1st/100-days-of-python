import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_resources():
    global money
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def process_user_choice(user_choice):
    if user_choice == "report":
        print_resources()
    elif user_choice =="off":
        machine_off = True
        sys.exit(0)
    elif user_choice in MENU:
        for resource in resources:
            if resources[str(resource)] < MENU[user_choice]['ingredients'][str(resource)]:
                print(f"Sorry there is not enough {resource}.")
                return
        for ingredient, amount in MENU[user_choice]['ingredients'].items():     # Deducting drink resources
            resources[ingredient] -= amount
        return "valid"
    else:
        print("Invalid input. Please choose from (espresso/latte/cappuccino).")


def process_coins(user_choice):
    global money

    quarters= int(input("How many quarters?: "))
    dimes= int(input("How many dimes?: "))
    nickles= int(input("How many nickles?: "))
    pennies= int(input("How many pennies?: "))

    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    change = round(total - MENU[user_input]['cost'], 2)
    if change >=0:
        print(f"Here is ${change} in change.")
        print(f"Here is your {user_choice} ☕️. Enjoy!")
        money += MENU[user_input]['cost']
    else:
        print("Sorry that's not enough money. Money refunded.")
machine_off = False
money = 0

while not machine_off:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    result =process_user_choice(user_input)
    if result == "valid":
        transaction_result =process_coins(user_input)
