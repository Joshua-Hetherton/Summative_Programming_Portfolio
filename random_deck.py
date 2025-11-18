"""Randomised algorithm 
Shuffles a standard deck of cards.
Present the order for the shuffled cards to the user.
"""

import random as rand

def create_deck():
    suits= ["♠", "♥", "♣", "♦"]
    numbers= ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    full_deck=[f"{suit}{number}" for suit in suits for number in numbers]
    return full_deck

"""An Algorithm that picks a random number 'k' between 1 and Unstruck number remaining in the deck
Starting from the 0, traverses sequentially , until it reaches an untruck card (and skipps over any struck cards)
Appends to shuffle output
Repeat untill all cards are struck
Has an O(n) time complexity

Explanation from Wikipedia (https://en.wikipedia.org/wiki/Fisher–Yates_shuffle)#The_modern_algorithm and 
https://www.geeksforgeeks.org/dsa/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm

"""
def Fisher_Yates_Shuffle(list):
    shuffled_list=list
    for i in range(len(shuffled_list)-1, 0,-1):
        j= rand.randint(0, i+1)
        shuffled_list[i], shuffled_list[j]= shuffled_list[j], shuffled_list[i]
    # print(shuffled_list)
    return shuffled_list
