rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice_shape = ["rock", "paper", "scissors"]
shapes = {"rock": rock, "paper": paper, "scissors": scissors}
result = ""


pc_choice = random.randint(0,2)
pc_choice_shape = choice_shape[int(pc_choice)]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
player_choice_shape = choice_shape[player_choice%3]

if (player_choice in [0,1,2]) == False:
    result = "You chose an invalid number. You lose."
else:
    print(f"\n \n {shapes[player_choice_shape]} \n")
    print(f"Computer chose: \n \n {shapes[pc_choice_shape]}")

#Determining who won the game
if (player_choice in [0,1,2]) == False:
    result = "You chose an invalid number. You lose."
elif player_choice_shape == pc_choice_shape:
    result = "It's a draw"
elif (player_choice_shape == "rock" and pc_choice_shape == "scissors") or (player_choice_shape == "paper" and pc_choice_shape == "rock") or (player_choice_shape == "scissors" and pc_choice_shape == "paper"):
    result = "You win"
elif (pc_choice_shape == "rock" and player_choice_shape == "scissors") or (pc_choice_shape == "paper" and player_choice_shape == "rock") or (pc_choice_shape == "scissors" and player_choice_shape == "paper"):
    result = "You lose"

print(result)

