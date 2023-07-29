############### Blackjack Project #####################


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




