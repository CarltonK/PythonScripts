'''
Define the deck of Cards
'''
 # Import random and card modules
from random import shuffle
from card import Card

class Deck():
    '''
    A deck of cards is a collection of 52 cards
    Create cards from below:-
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
    'Ten', 'Jack', 'Queen', 'King', 'Ace')
        '''
    def __init__(self):

        # Initialize an empty list that will hold all 52 possible combinations
        self.deck = []

        # Possible combinations
        self.suit = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                     'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

        # Store a single card as a dictionary and append to self.deck
        for suit in self.suit:
            for rank in self.rank:
                singular_card = {suit:rank}
                self.deck.append(singular_card)

        # Add two Jokers to deck of Cards
        # A joker has a value of say 1000
        joker = {'Joker':'Okota'}
        # Add two to complete deck
        self.deck.append(joker)
        self.deck.append(joker)

        #print(self.deck)
    def shuffle_deck(self):

        '''
        Shuffle the deck of cards
        Shuffle five times if necessary
        '''
        shuffle(self.deck)
        shuffle(self.deck)
        shuffle(self.deck)
        shuffle(self.deck)
        shuffle(self.deck)

    def deal(self):

        '''
        Return a random card
        '''

        self.shuffle_deck()
        dealt_card = self.deck.pop()
        #print('You have picked {}'.format(Card(dealt_card)))
        return dealt_card



    def __str__(self):
        '''
        Print a single card
        '''
        return '{}'.format(self.deck)

'''
d = Deck()
print(d)
d.deal()
'''
