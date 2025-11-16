import random
from art import logo
answer = random.randint(1,100)

def print_attempts():
    print(f"You have {attempts} attempts remaining to guess the number")

def evaluate_guess(guess):
   global attempts
   if guess> answer:
      print("Too high.")
   elif guess < answer:
      print("Too low.")

   print("Guess again")
   attempts -=1
   print_attempts()
   guess= int(input("Make a guess: "))
   return guess

print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
# print(f"The answer is {answer}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

print_attempts()
guess= int(input("Make a guess: "))

while guess != answer and attempts >1:    ## attempts >1 since attempts are updated after the evaluate_guess() is called
    guess =evaluate_guess(guess)

if guess == answer:
    print(f"You got it! The answer was {answer}.")
else:
    print("You've run out of guesses, you lose.")
