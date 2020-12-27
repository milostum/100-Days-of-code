from art import logo
from random import randint

print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of number between 1 and 100.")

secret_number = randint(1, 100)
#print(f"Pssst, the correct answer is {secret_number}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == 'easy':
    attempts = 10
else:
    attempts = 5

def game(x):
    print(f"You have {x} attempts remaining to guess the number.")
    while x > 0:
        guess = int(input("Make a guess: "))
        if guess > secret_number:
            x -= 1
            print("Too high.")
        elif guess < secret_number:
            x -= 1
            print("Too low.")
        else:
            print(f"You got it! The answer was {secret_number}.")
            break
        
        if x > 0:
            print(f"Guess again. \nYou have {x} attempts remaining to guess the number.")
        else:
            print("You've run out of guesses, you lose.")

game(attempts)
