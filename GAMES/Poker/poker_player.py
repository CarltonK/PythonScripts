'''
Initiate a single poker player
'''
from deck import Deck
from hand import Hand

class Player():
    '''
    The player has a name and list
    The list contains cards
    '''
    def __init__(self, p_name, p_hand=[], p_value=0):
        '''
        P_hand is a list representing the players current hand
        Eg: p_hand=[{'Hearts':'Two'},{'Spades':'Jack'},..]
        '''
        self.p_name = p_name
        self.p_hand = p_hand
        self.p_value = p_value

        self.p_value = self.player_value()

    def pick_card(self):
        '''
        Pick a card from deck
        Pop from deck, show popped card and add to player hand
        '''
        self.p_hand.append(Deck().deal())
        self.p_value = self.player_value()

    def player_value(self):
        '''
        Show the value of the hand
        '''
        hand_alpha_list = []
        for val in self.p_hand:
            value_alpha = list(val.values())
            hand_alpha_list.append(value_alpha[0])

        # print(hand_alpha_list)
        # Initialize the total value
        total_value = 0
            # Iterate through the list to get rank
        for i_value in hand_alpha_list:
            if i_value == 'Two':
                value_num = 50
            elif i_value == 'Three':
                value_num = 75
            elif i_value == 'Four':
                value_num = 4
            elif i_value == 'Five':
                value_num = 5
            elif i_value == 'Six':
                value_num = 6
            elif i_value == 'Seven':
                value_num = 7
            elif i_value == 'Eight':
                value_num = 8
            elif i_value == 'Nine':
                value_num = 9
            elif i_value == 'Ten':
                value_num = 10
            elif i_value == 'Jack':
                value_num = 10
            elif i_value == 'Queen':
                value_num = 10
            elif i_value == 'King':
                value_num = 10
            elif i_value == 'Ace':
                value_num = 100
            elif i_value == 'Okota':
                value_num = 500

            total_value += value_num
        #print('HAND VALUE: {}'.format(total_value))
        return total_value



    def __str__(self):
        return 'NAME: {}\nHAND: {}\nVALUE: {}'.format(
                self.p_name, self.p_hand, self.p_value
        )
'''
...TEST...
name = input('What is your name? ')
cadi_list = [{'Hearts':'Two'},]
p = Player(name, cadi_list)
p.pick_card()
p.pick_card()
print(p)
'''
