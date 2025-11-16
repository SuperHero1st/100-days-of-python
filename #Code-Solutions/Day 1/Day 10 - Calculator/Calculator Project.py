import os
from calc_art import logo
def add (n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations= {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator(num1,num2, operation):

    caclculation_func = operations[operation]
    answer = caclculation_func(num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    return answer


def user_input(answer):
    if answer == "":
        num1 = float(input("What's the first number?: "))
    else:
        num1= answer
    for operation in operations:
        print (operation)
    chosen_operation_symbol = input("Pick and operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    answer = calculator(num1, num2, chosen_operation_symbol)
    return answer

more_calculation = True
print(logo)

while more_calculation:
    answer = user_input("")
    exit_or_continue= input(f"Type 'y' to continue calculating with {answer}, or type'n' to exit.: ")
    if exit_or_continue == "y":
        user_input(answer)
    else:
        more_calculation = False
        os.system('cls')
        user_input("")
 
