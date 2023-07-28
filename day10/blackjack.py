############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import art_blackjack
import random

print(art_blackjack.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_playing = True
hit_me = True




def deal_initial():
    '''At start of game deal player 2 cards and dealer one card. Store result
      in a dictionary'''
    dealt = []
    for card in range(3):
        rand_num = random.randint(0, 12)        
        card = cards[rand_num]
        dealt.append(card)
    player_score = dealt[0] + dealt[1]
    dealer_score = dealt[2]
    table_status = {
        'player': [dealt[0], dealt[1]],
        'player_score': player_score,
        'dealer': [dealt[2]],
        'dealer_score': dealt[2]
        }
    return table_status

def deal_card():
    ''' Returns a random card from deck'''
    card_index = random.randint(0, 12)
    card = cards[card_index]
    return card

def add_score():
    '''Adds up the card in the players hand checking for ace and ajusting as 
     necessary if over 21 and updates player score'''
    def add_cards(player_name):
        player_score = 0 
        player_has_ace = False
        if 11 in dealt[player_name]:
            player_has_ace = True               
        for card in dealt[player_name]:            
            player_score += card
        if  player_score > 21 and player_has_ace:
            player_score -= 10            
        return player_score     

    dealt['player_score'] = add_cards('player')
    dealt['dealer_score'] = add_cards('dealer')

def print_score():
    if hit_me:     
        print(f"Your cards: {dealt['player']}, current score: {dealt['player_score']}")
        print(f"Computer's first card: {dealt['dealer'][0]}")
    else:
        print(f"Your final hand: {dealt['player']}, final score: {dealt['player_score']}")
        print(f"Computer's final hand: {dealt['dealer']}, final score: {dealt['dealer_score']}")

def finish_dealing():
    '''When player finished. Deal dealer cards until > 16. Update score'''
    while dealt['dealer_score'] < 17:
        card = deal_card()
        dealt['dealer'].append(card)
        add_score()

def has_blackjack(player_name):
    name = player_name + "_score"
    player_score = dealt[name]
    if 11 in dealt[player_name] and player_score == 21 and len(dealt[player_name]) == 2:
        return True
    return False

def print_final_result():
    '''Check for winner'''
    player_final_score = dealt['player_score']
    dealer_final_score = dealt['dealer_score']
    if has_blackjack('dealer'):
        print("Dealer has blackjack. You lose")
    elif has_blackjack('player'):
        print("You've Blackjack. You win.")    
    elif player_final_score > 21:
        print("You went over. You lose")
    elif dealer_final_score > 21:
        print("Dealer went bust. You win")
    elif  dealer_final_score <= 21 and player_final_score > dealer_final_score:
        print("You win")
    elif dealer_final_score == player_final_score:
        print("It's a draw")
    else:
        print("You lose")







dealt = deal_initial()
print_score()


while hit_me:
    another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if another == "y":
        card = deal_card()
        dealt['player'].append(card)
        add_score()
        print_score()
        if dealt['player_score'] > 21:
            hit_me = False 
            finish_dealing()
            add_score()
            print_score() 
    else:
        hit_me = False
        finish_dealing()
        add_score()
        print_score()

print_final_result()




