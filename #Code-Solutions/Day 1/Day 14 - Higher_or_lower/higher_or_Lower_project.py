from game_data import data
from art import logo, vs
import random, os

def print_page_info(data, A_title):

    """"Takes a dictionary of page information, prints them one by one. Returns followers counts"""

    random_page = data[A_title]
    print(f"Compare A: {random_page['name']}, {random_page['description']}, from {random_page['country']}")
    A_followers_count = random_page['follower_count']

    print(vs)


    B_title_index = random.randint(0,49)
    while B_title_index in used_titles:
        B_title_index = random.randint(0,49)            # Making user a title doesn't repeat

    random_page = data[B_title_index]
    print(f"Against B: {random_page['name']}, {random_page['description']}, from {random_page['country']}")
    B_followers_count = random_page['follower_count']
    used_titles.append(B_title_index)

    return A_followers_count, B_followers_count, B_title_index

def game(A_title_index, score):
    """"Takes the A_Title index , Starts the game and returns the B_index """
    game_over = False
    A_followers_count, B_followers_count, old_B_title_index=  print_page_info(data, A_title_index)
    game_choice = input("Who has more followers? Type 'A' or 'B': ")

    if (game_choice.lower() == "a" and A_followers_count > B_followers_count) or (game_choice.lower() == "b" and A_followers_count < B_followers_count):       # User is correct
        os.system('cls')
        score +=1
        print(logo)
        print(f"You're right! Current score: {score}.")
    else:
        os.system('cls')
        game_over = True
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")

    return old_B_title_index, score, game_over

used_titles = []
A_title_index = random.randint(0,49)
used_titles.append(A_title_index)
score = 0
game_over= False

while not game_over:
    A_title_index, score, game_over = game(A_title_index, score)
