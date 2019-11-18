'''
Initiate a single poker player
'''
class Player():
    '''
    The player has a name and list
    The list contains cards
    '''
    def __init__(self, p_name, p_hand=[]):
        '''
        P_hand is a list representing the players current hand
        Eg: p_hand=[{'Hearts':'Two'},{'Spades':'Jack'},..]
        '''
        self.p_hand = p_hand

    def pick_card(self):
        '''
        Pick a card from deck
        Pop from deck, show popped card and add to player hand
        '''
        pass

    def player_value(self):
        '''
        Calculate player value to determine who continues in the game,
        in the event of a win
        '''
        pass
