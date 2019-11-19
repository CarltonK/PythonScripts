'''
Define a single card
They will be combined to form a deck
'''
class Card():
    '''
    Initialize a single card
    Card attributes are 'suit' and 'rank'
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
    'Ten', 'Jack', 'Queen', 'King', 'Ace')
    '''

    def __init__(self, s_card={}):
        '''
        dictionary
        s_card = {suit:rank}
        print(s_card) = rank of suit. Eg: Three of Hearts
        '''
        self.s_card = s_card
        self.suit = list(self.s_card.keys())[0]
        self.rank = self.s_card[self.suit]

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)


'''

...TEST...
c = Card({'Spades':'Jack'})
help(c)
print(c)
'''
