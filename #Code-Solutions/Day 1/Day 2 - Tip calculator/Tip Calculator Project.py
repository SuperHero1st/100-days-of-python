print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15?  "))
number_of_people = int(input("How many people to split the bill?  "))

final_amount = (bill + bill * tip_percent/100)  / number_of_people

result = round((bill + bill * tip_percent/100)  / number_of_people, 2)
result = "{:.2f}".format(final_amount) # Formatting function that makes two digits appear in the floating number

print(f"Each person should pay: ${result}")
1