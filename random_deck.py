"""Randomised algorithm 
Shuffles a standard deck of cards.
Present the order for the shuffled cards to the user.
"""

import random

def create_deck():
    suits= ["Spades", "Hearts", "Clubs", "Diamonds"]
    numbers= ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    full_deck=[f"{number} of {suit}" for suit in suits for number in numbers]
    return full_deck

"""An Algorithm that picks a random number 'k' between 1 and Unstruck number remaining in the deck
Starting from the 0, traverses sequentially , until it reaches an untruck card (and skipps over any struck cards)
Appends to shuffle output
Repeat untill all cards are struck

"""
def Fisher_Yates_Shuffle():
    pass
