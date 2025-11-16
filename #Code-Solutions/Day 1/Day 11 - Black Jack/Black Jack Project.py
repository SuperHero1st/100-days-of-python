import os, random, sys
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start_game():
    user_choice = get_choice("start")                     ## Asking if he wants to play

    if user_choice == "y":
        os.system('cls')
        print(logo)
    else:
        os.system('cls')
        print("Good Bye")
        sys.exit()

def get_choice(current_choice):
    if current_choice =="start":
        user_choice= input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        return user_choice
    elif current_choice =="1morecard":
        user_choice= input("Type 'y' to get another card, type 'n' to pass: ")
        return user_choice

def draw_cards_1st():
    user_cards=[]
    computer_cards=[]
    for i in range(2):
        random_card = random.choice(cards)
        user_cards.append(random_card)
        random_card = random.choice(cards)
        computer_cards.append(random_card)
    return user_cards, computer_cards

def calc_score(cards):
    return sum(cards)

def one_and_eleven_check(cards_list):
    check = False
    if 11 in cards_list and calc_score(cards_list)> 21:
        index =cards_list.index(11)
        cards_list[index] = 1
        check = True

def show_all_cards():
    one_and_eleven_check(user_cards)
    one_and_eleven_check(computer_cards)
    print(f"    Your cards: {user_cards}, current score: {calc_score(user_cards)}")
    print(f"    Computer's first card: {computer_cards[0]}")

def add_card(cards_list):
    random_card = random.choice(cards)
    cards_list.append(random_card)

def final_score():
    user_score= calc_score(user_cards)
    computer_score= calc_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    if user_score > 21 and computer_score< user_score:
        print("You went over. You lose 😭")
    elif computer_score > user_score and computer_score <=21:
        print("You lose 😤")
    elif computer_score == user_score:
        print("Draw")
    else:
        print("Opponent went over. You win 😁")


def calc_computer_final_deck():
    computer_score= calc_score(computer_cards)
    if computer_score <16 :                     ## BlackJack Rule
        add_card(computer_cards)

    computer_score= calc_score(computer_cards)
    while user_score <= 21 and computer_score <=17 and computer_score < user_score :
        add_card(computer_cards)
        computer_score= calc_score(computer_cards)


while True:
    print(logo)
    user_cards, computer_cards = draw_cards_1st()         ## Step only at the beginning

    start_game()
    show_all_cards()

    user_score= calc_score(user_cards)
    user_choice = get_choice("1morecard")

    while user_score <=21 and user_choice == "y":
        add_card(user_cards)
        one_and_eleven_check(user_cards)
        user_score= calc_score(user_cards)
        show_all_cards()
        if user_score<=21:
            user_choice = get_choice("1morecard")

    calc_computer_final_deck()
    final_score()
    start_game()




