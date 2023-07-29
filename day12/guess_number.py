# Guessing number game where the computer chooses a number between 1 and 100
# and you get 5 or 10 guesses based on difficulty level choosen. 

import random
import art



def guess_number():
    print(art.logo)
    number = random.randint(1, 100)
    lives = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    
    while lives > 0:
        print(f"You've {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess."))
        if guess != number:
            lives -= 1
            if guess > number:
                print("Too high.")
            else:
                print("Too low.")
            if lives > 0:
                print("Guess again")
            else:
                print("You lose.")
        else:
            print("You got it. You win.")
            return
    
guess_number()
