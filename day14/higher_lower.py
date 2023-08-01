''' Higher Lower game using celebrity instagram followers'''
from random import choice
from art import logo_higher, logo_vs
from followers import celebrity_instagram_data


def get_random_celeb():
    '''Gets a random celeb from dictionary and returns a list'''
    celeb_name, info = choice(list(celebrity_instagram_data.items()))
    return [celeb_name, info]


def get_unique_celeb(store):
    ''' Gets a random celeb and checks to see if already in store. If not
    keeps getting random until unique'''
    while True:
        new_celeb = get_random_celeb()
        # check all names in store. If match new_celeb get new celeb
        if new_celeb not in store.values():
            return new_celeb


def most_followers(store):
    '''Returns celeb with most followers '''
    if store["A"][1]["followers"] > store["B"][1]["followers"]:
        return "A"
    return "B"

def compare_celebs(guess, store, score):
    '''Check if guess has most followers and return true or false'''
    if guess == most_followers(store):
        store.pop(guess)
        score += 1
        store[guess] = get_unique_celeb(store)
        return True
    else:
        return False


def play_game():
    ''' Play game of higher lower and loop until player gets one wrong'''
    score = 0
    store = {}
    store["A"] = get_unique_celeb(store)
    store["B"] = get_unique_celeb(store)
    player_right = True

    while player_right:
        # print logo1 and celeb A info        
        print(logo_higher)
        if score != 0:
            print(f"You're right!. Current score: {score}")
        print(f"Compare A: {store['A'][0]} a {store['A'][1]['profession']}, from {store['A'][1]['country']}")
        # print logo2 and celeb B info
        print(logo_vs)

        print(f"Against B: {store['B'][0]} a {store['B'][1]['profession']}, from {store['B'][1]['country']}")
        # Ask for who has more followers and store answer
        guess = input("Who has more followers? Type 'A' or 'B': ")

        # Check if right, if right add 1 to score and ask for another. If wrong end 
        if compare_celebs(guess, store, score):
            score += 1    
            print(f"You're right!. Current score is: {score}")
            # If wrong print thats wrong your final score is
        else:
            player_right = False
            print (f"Sorry that's the wrong answer. Final score: {score}")

play_game()
