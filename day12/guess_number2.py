# import and print logo
from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5
 
# set difficulty level
def set_difficulty():
    '''Sets level based on user choice and returns the number of lives as int'''
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    return HARD_LEVEL

#check guess and print the number of lives left

def check_guess(guess, number,lives):
    '''Check guess, print response, update lives and return lives left'''
    if guess != number:
        lives -= 1        
        if guess > number:
            print('Too high.')
        else:
            print("Too low.")
    else:
        print("You got it. You won.")
    return lives

def guess_number():
    print(logo)   
    # get a random number and print starting info
    number = randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    lives = set_difficulty()

    #loop untill lives = 0 or get it right
    guess = 0
    while guess != number:
        print(f"You have {lives} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lives =  check_guess(guess, number, lives)
        if lives > 0:
            print("Guess again.")
        else:
            print("You've run out of guesses. You lose.")
            return
        
        


guess_number()
