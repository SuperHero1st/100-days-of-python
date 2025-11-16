print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island. \nYour mission is to find the treasure. ")
direction = input("You're at a cross road. Where do you want to go? \n")


if direction.lower() == "left":

  print("\nYou've come to a lake. There is an island in the middle of the lake. ")
  swim_or_wait = input('  Type "wait" to wait for a boat. Type "swim" to swim across. \n')

  if swim_or_wait.lower() == "wait":

    print("You arrive at the island unharmed. There is a house with 3 doors. ")
    chosen_color = input("  One red, one yellow and one blue. Which colour do you choose? \n")

    if chosen_color.lower() == "red":
      print("\nIt's a room full of fire. \nGame Over.")
    elif chosen_color.lower() == "blue":
      print("\nYou're eaten by the beasts. \nGame Over.")
    elif chosen_color.lower() == "yellow":
      print("\nYou Win!")
    else:
      print("\nGame Over.")
  else:
     print("\nYou get attacked by an angry trout. Game Over.")
else:
  print("\nYou fell into a hole. \nGame Over.")
    
    
  