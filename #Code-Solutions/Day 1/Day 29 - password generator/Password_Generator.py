from random import randint, choice, shuffle
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")

    selected_letters = []
    selected_symbols = []
    selected_numbers = []

    selected_letters = [choice(letters) for letter in range(randint(8, 10))]
    selected_numbers = [choice(numbers) for number in range(randint(2, 4))]
    selected_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_list = selected_letters + selected_symbols + selected_numbers

    shuffle(password_list)
    password = "".join(password_list)
    return password