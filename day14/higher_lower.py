from art import logo_higher, logo_vs
from followers import celebrity_instagram_data
from random import choice

# get 2 random celebs form data, store order of each as A and B 
# each guess B becomes A and B gets new random celeb
score = 0
store = {} 
def get_random_celeb():
    '''Gets a random celeb from dictionary and returns a list'''
    celeb_name, info = choice(list(celebrity_instagram_data.items()))
    return [celeb_name, info]

def get_unique_celeb():
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
    # opposite = "B" if guess == "A" else "A"    
    if guess == most_followers(store):
        store.pop(guess)
        score += 1
        store[guess] = get_unique_celeb()
        return True        
    else:
        return False
        # print (f"Sorry that's the wrong answer. Final score: {score}")




def play_game(store, score):
    store["A"] = get_unique_celeb()
    store["B"] = get_unique_celeb()
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

play_game(store, score)