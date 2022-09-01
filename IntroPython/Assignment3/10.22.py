# Coupon Collector is a classic statistics problem with many practical applications.
# The problem is to pick objects from a set of objects repeatedly and find out how many picks are needed
# for all the objects to be picked at least once. A variation of the problem is to pick cards from a shuffled
# deck of 52 cards repeatedly and find out how many picks are needed before you see one of each suit. Assume
# a picked card is placed back in the deck before picking another. Write a program to simulate the number of
# picks needed to get four cards, one from each suit and display the four cards picked (it is possible a card
# may be picked twice).

import random

deck = [x for x in range(52)]

random.shuffle(deck)

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

found_suits = []
picks = 0
while len(found_suits) < 4:
    picks += 1
    card = random.randint(0, 51)
    suit = suits[deck[card] // 13]
    rank = ranks[deck[card] % 13]
    if suit not in found_suits:
        found_suits.append(suit)
        print("Card number", deck[card], "is the", rank, "of", suit)
print("Number of picks: ", picks)