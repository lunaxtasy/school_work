"""
ASSIGNMENT 5 - BLACKJACK

This program plays Blackjack with you.

To run this program, use python assignment_5_rebecca_doran.py
"""

from random import randint, shuffle

"""
Card_deck Class

This class generates the card deck using 1 - 10.
There are 4 of each number in the deck. It'll also
shuffle the deck. When requested, it'll also randomly
draw a card.
"""

class Card_deck:

    def card_deal(self, amount):

        from random import shuffle

        #Creates deck and shuffles it
        card_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4
        shuffle(card_num)
        drawn = []

        #Adds random card from card_num list to drawn list and removes it from card_num
        for _ in range(amount):
            drawn.append(card_num.pop(randint(0, len(card_num) - 1)))

        #Returns values in list called drawn
        return drawn

"""
Player Class

This class sets the player's hand through
calling the Card_deck class.
It also provides logic for bust situations
"""

class Player(Card_deck):

    hand = []
    bust = False
    score = 0

"""
Dealer Class

This class sets the dealer's hand through
calling the Card_deck class
It also provides logic for bust situations
and scorekeeping
"""

class Dealer(Card_deck):

    hand = []
    bust = False
    score = 0

"""
hand_value

Calculates the total of the cards in each hand
for use in assessing who has won the hand.
"""

def hand_value(hand):

    total = 0
    total_value = []

    #Adds all cards from a hand to list for addition
    for x in range(len(hand)):
        total_value.append(hand[x])

    #Calculates hand value
    for x in range(len(total_value)):
        total += total_value[x]

    #Returns total value of hand when pulled by dealer or player
    return total

#Shortcut calls for accessing prefined class and function calls
play = Player()
deal = Dealer()

while True: #will be true while player chooses to play

    #Welcome and dividers for easier viewing
    divider = "*"
    welcome = "WELCOME TO BLACKJACK"
    space = " "

    print(f"{divider:*^100}")
    print(f"{welcome: ^100}")
    print(f"{divider:*^100}")

    #Deals hands for both dealer and player
    play.hand = play.card_deal(2)
    deal.hand = deal.card_deal(2)
    #Print player's and dealer's hands. Second card hidden for dealer
    #Totals value of player's hand
    print(f"You drew a(n) {play.hand[0]} and a(n) {play.hand[1]}")
    print(f"The dealer drew a(n) {deal.hand[0]} and one hidden card")
    play_total = hand_value(play.hand)
    print(f"Your current total is {play_total}")
    print(f"{divider:*^100}")

    """
    hard resets for answer logic
    """
    win_deal = False #Will become True when conditions for dealer winning occur
    tiebreak = False #Will become True when both player and dealer have the same hand value
    play.bust = False #Will become True when player's hand value is over 21
    deal.bust = False #Will become True when dealer's hand value is over 21

    """
    Error checking for answer logic

    print(win_deal)
    print(tiebreak)
    print(play.bust)
    print(deal.bust)
    """

    while True: #Will be true while player continues to draw cards

        while True: #Will be true while player chooses to hit or stand

            #Asks if player for like to hit or stand to continue gameplay
            try:
                next_turn = input(f"\nWould you like to draw another card? [h = hit / s = stand]: ")
                #Casts to lower case and checks if entered input is h or s. Raises exception if it is not
                if next_turn.lower() not in ["h", "s"]:
                    raise Exception
                break
            #Exception for any entry that is not an h or a s
            except Exception:
                print(f"\nERROR!!!! Invalid selection made! Would you like to draw another card? [h = hit / s = stand]: ")
        #Draws one new card into hand if h is entered and totals new value
        if next_turn.lower() == "h":
            play.hand += play.card_deal(1)
            play_total = hand_value(play.hand)
            print(f"You chose HIT! You have drawn a(n) {play.hand[-1]}. Your total is now {play_total}.")
        #Breaks out of hit loop if s is entered
        else:
            break

        #Will not trigger following if statements if hand value is less than 21 when s entered
        #Automatically breaks hit loop if total value of hand is equal to 21. No logic triggered
        if play_total == 21:
            break
        #Automatically breaks hit loop if total value of hand exceeds 21
        #Sets logic to trigger bust and win_deal logic
        elif play_total > 21:
            play.bust = True
            win_deal = True
            break

    #Runs if win_deal has not been toggled to True during player's turn
    if not win_deal:

        #Provides final tally of player's hand before progressing to dealer's turn
        print(f"\nAww... You chose stand. Your final total is: {play_total}")
        print(f"{divider:*^100}")
        #calculates value of dealer's hand including hidden card and displays
        deal_total = hand_value(deal.hand)
        print(f"\nThe dealer's hidden card is......... a(n) {deal.hand[1]}, for a total of {deal_total}")

        #Loops until the value of the dealer's hand is over 16 and then sets result logic
        while True:
            #Draws card and retotals hand until value of hand is over 16
            if deal_total < 17:
                deal.hand += deal.card_deal(1)
                deal_total = hand_value(deal.hand)
                print(f"The dealer hits and draws a(n) {deal.hand[-1]}. Their total is {deal_total}")
            #Breaks loop once dealer's hand is 17 or higher
            else:
                print(f"\nThe dealer stands! The dealer's final total is: {deal_total}")
                break

            #Logic setting for result scenerios. Only one not hard coded is when the player's hand is higher
            #in value than the dealer's
            #Toggles logic for dealer bust when dealer's hand is over 21
            if deal_total > 21:
                deal.bust = True
                break
            #Toggles logic for tie and dealer win when both dealer and player tie
            elif deal_total == play_total:
                win_deal = True
                tiebreak = True
                break
            #Toggles dealer win when the value of the dealer's hand is greater than the player's
            elif deal_total > play_total:
                win_deal = True
                break

    """
    Error checking for answer logic
    print(win_deal)
    print(tiebreak)
    print(play.bust)
    print(deal.bust)
    """
    #Assessment for win scenerios, also increments score accordingly
    #Scenerios with win_deal set to True, dealer wins
    if win_deal:
        #Player hand value over 21
        if play.bust == True:
            print(f"{divider:*^100}")
            print(f"\nYOU LOSE! Your hand's value is greater than 21! Congratulations to the dealer!")
            deal.score +=1
        #Dealer and player both tied
        elif tiebreak == True:
            print(f"{divider:*^100}")
            print(f"\nYOU LOSE! The dealer wins when both dealer and player are tied with {deal_total}")
            deal.score += 1
        #Dealer has hand value higher than player's up to a maximum of 21
        else:
            print(f"{divider:*^100}")
            print(f"\nYOU LOSE! The dealer wins with {deal_total} versus your hand of {play_total}!")
            deal.score += 1
    #Scenerios with win_deal set to False, player wins
    else:
        #Dealer hand value over 21
        if deal.bust == True:
            print(f"{divider:*^100}")
            print(f"\nYOU WIN! The dealer's hand's value is greater than 21!")
            play.score += 1
        #Player has hand value higher than dealer's up to a maximum of 21
        else:
            print(f"{divider:*^100}")
            print(f"\nYOU WIN! Your hand is {play_total} versus the dealer's hand of {deal_total}!")
            play.score += 1

    #Winner declared
    while True:
        try:
            #Get player input for playing again. Must be y or n otherwise exception is raised
            #Casts player input to lower case
            print(f"{divider:*^100}")
            play_again = input(f"\nWould you like to play again [y = yes / n = no]: ")
            #Triggered exception when player input is not y or n
            if play_again.lower() not in ["y", "n"]:
                raise Exception
            break
        #Raised exception
        except Exception:
            print(f"\nERROR!!!! Invalid selection made! Would you like play again? [y = yes / n = no]: ")

    """
    Scoreboard

    Quick visual reference for tracking who wins
    over multiple games (because who doesn't want
    to know)
    """
    print(f"{divider:*^100}")
    print(f"{space:^22}PLAYER{space:^22}::{space:^22}DEALER{space:^22}")
    print(f"{space:^25}{play.score}{space:^24}::{space:^24}{deal.score}{space:^25}")
    print(f"{divider:*^100}")

    #Prints appropriate message depending on who is winning
    #Player winning
    if play.score > deal.score:
        print(f"The Player is currently winning!")
    #Dealer winning
    elif play.score == deal.score:
        print(f"The score is tied!")
    #Player and dealer tied
    else:
        print(f"The Dealer is currently winning")

    #Exits game when n is entered by player
    if play_again.lower() == "n":
        print(f"\nThank you for playing! Goodbye!")
        exit()
