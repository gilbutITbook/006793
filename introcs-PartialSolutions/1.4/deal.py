#-----------------------------------------------------------------------
# deal.py
#-----------------------------------------------------------------------

import stdio
import sys
import random

# Accept integer playerCount as a command-line argument. Deal 5-card
# hands at random to playerCount players. Write the hands to standard
# output.

CARDS_PER_PLAYER = 5

playerCount = int(sys.argv[1])

# Initialize the deck.
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', \
    'Jack', 'Queen', 'King', 'Ace']
deck = []
for rank in ranks:
    for suit in suits:
        card = rank + ' of ' + suit
        deck += [card]

# Shuffle the deck.
for i in range(len(deck)):
    r = random.randrange(i, len(deck))
    temp = deck[r]
    deck[r] = deck[i]
    deck[i] = temp

# Write cards from the shuffled deck.
deckIndex = 0
for i in range(playerCount):
    for j in range(CARDS_PER_PLAYER):
        stdio.writeln(deck[deckIndex])
        deckIndex += 1
    stdio.writeln()
    
#-----------------------------------------------------------------------

# python deal.py 1              
# 10 of Hearts
# 7 of Clubs
# 9 of Diamonds
# Queen of Hearts
# 3 of Spades

# python deal.py 4
# Jack of Hearts
# Queen of Hearts
# 7 of Spades
# 3 of Hearts
# 5 of Clubs
# 
# King of Diamonds
# Queen of Spades
# 8 of Hearts
# 9 of Diamonds
# 6 of Spades
# 
# 3 of Diamonds
# 9 of Clubs
# Jack of Spades
# 9 of Spades
# 5 of Hearts
# 
# Queen of Diamonds
# 10 of Clubs
# 2 of Clubs
# King of Hearts
# 5 of Diamonds

