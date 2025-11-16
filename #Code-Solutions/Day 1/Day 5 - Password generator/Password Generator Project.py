import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


selected_letters = []
selected_symbols = []
selected_numbers = []

#Eaسy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for letter in range (0, nr_letters):
    selected_letters.append(letters[random.randrange(0, len(letters)-1)])

for number in range (0, nr_numbers):
    selected_numbers.append(numbers[random.randrange(0, len(numbers)-1)])

for symbol in range (0, nr_symbols ):
    selected_symbols.append(symbols[random.randrange(0, len(symbols)-1)])

password = selected_letters + selected_symbols + selected_numbers

################# Easy Level ################

print("".join(password))

################# Hard Level ################

# We could just use ->   random.shuffle(password)

hard_password = []
 
for digit in range(0,len(password)):
    random_index= random.randint(0,len(password)-1)
    random_digit= password[random_index]
    hard_password.append(random_digit)
    password.pop(random_index)

print("".join(hard_password))
