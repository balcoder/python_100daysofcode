import os
import art
#HINT: You can call os.system('cls') on windows or os.system('clear') on linux to clear the output in the console.
print(art.logo)
more_bidders = True
bids = {}

def find_highest_bidder(bids_dictonary):
    # more_bidders = False
    best_bid = 0
    best_bidder =""
    for person in bids_dictonary:
        if int(bids_dictonary[person]) > int(best_bid):
            best_bidder = person
            best_bid = bids[person]    
    os.system('cls')
    print(f"The winning bidder is {best_bidder} with a bid of ${best_bid}") 

while more_bidders:
    name = input("What is your name?\n")
    bid = input("What is your bid?\n")
    bids[name] = bid
    more_bids = input("Are ther more bidders Yes/No\n".lower())
    # more bids
    if more_bids == "yes":
        os.system('cls')
    else:
        more_bidders = False
        find_highest_bidder(bids)
        # more_bidders = False
        # best_bid = 0
        # best_bidder =""
        # for person in bids:
        #     if int(bids[person]) > int(best_bid):
        #         best_bidder = person
        #         best_bid = bids[person]    
        # os.system('cls')
        # print(f"The winning bidder is {best_bidder} with a bid of ${best_bid}")        