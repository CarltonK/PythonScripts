'''
Cards in players possession
'''
class Hand():

    '''
    Show current
    '''

    def __init__(self):
        self.hand = []

    def add_card(self, card):
        '''
        Adding card to the hand
        '''
        self.hand.append(card)
        print('CURRENT HAND\n............\n{}'.format(self.hand))

    def __str__(self):
        '''
        Print the hand of the player
        '''
        return 'CURRENT HAND\n............\n{}'.format(self.hand)


    def __len__(self):
        '''
        Return the number of cards in a player's hand
        '''
        return len(self.hand)


'''
...TEST...
h = Hand()
h.add_card({'Hearts':'Two'})
h.add_card({'Hearts':'Five'})
h.add_card({'Joker':'Okota'})
print(h)
print(h.hand_value())
'''
