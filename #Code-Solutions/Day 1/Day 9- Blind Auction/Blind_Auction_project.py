import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
more = True
bidders={}
max_bid= 0

while more:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    more_bidders = input("Are there any other bidders? Type 'yes or 'no'.")

    bidders[name]= bid
    

    if more_bidders.lower() == "yes":
        os.system('cls')
    else:
        more = False
        for name in bidders:
            if bidders[name]> max_bid:
                max_bid = bidders[name]
                winner = name
        print(f"The winner is {winner} with a bid of ${max_bid}")
