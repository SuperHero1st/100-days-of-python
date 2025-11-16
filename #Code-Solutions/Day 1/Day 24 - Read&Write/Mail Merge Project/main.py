with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

with open("./Input/Names/invited_names.txt") as names:
    names_list = [line.strip() for line in names.readlines()]

for name in names_list:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
        new_content = letter.replace("[name]", name)
        new_letter.write(new_content)


















#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
