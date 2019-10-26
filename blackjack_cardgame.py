# Player Class
class Player:
    '''
    Initialize Player
    '''
    def __init__(self):
        self.name = input('Enter you name: ')
        print('Welcome to the game {}'.format(self.name))


    def bet_stake(self):

        while True:
            try:
                self.stake = int(input('How much would you like to stake? '))
                self.bet = int(input('How much are you willing to bet? '))
            except:
                print('Invalid Entry...Try Again')
                continue
            else:
                if self.bet > self.stake:
                    print('You cannot bet more than {}'.format(self.stake))
                    continue
                else:
                    print('You have placed a bet for {}'.format(self.bet))
                    break

    def lose_bet(self):
        self.stake -= self.bet
        print('Casino Wins. You Lose.')
        print('Your balance is: {}'.format(self.stake))

    def win_stake(self):
        self.stake += self.bet * 2
        print('Congratulations. Winner')
        print('Your balance is: {}'.format(self.stake))

    def __str__(self):

        return self.name

# Dealer Class
class Dealer():

    '''
    Initialize the Dealer
    '''

    def __init__(self):
        self.balance = 10000
        print('The dealer is ready')
        print()


# Card Class
class Card:
    '''
    Initialize a single card
    Card attributes are 'suit','rank' and 'value'
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    '''

    def __init__(self):

        self.suit = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


        '''import random
        self.suit = random.choice(self.suit)
        self.rank = random.choice(self.rank)
        '''

    def __str__(self):
        return ('{} of {}'.format(self.rank,self.suit))

# Deck Class

import random
class Deck:

    '''
    A deck of cards has 52 cards
    '''

    def __init__(self):

        # Initialize an empty list that will hold all 52 possible combinations
        self.deck = []

        # Initiatialize card class
        card = Card()

        # Store a single card as a dictionary and append to self.deck
        for suit in card.suit:
            for rank in card.rank:
                singular_card = {suit:rank}
                self.deck.append(singular_card)

        #print(self.deck)
    def shuffle_deck(self):

        '''
        Shuffle the deck of cards
        '''

        random.shuffle(self.deck)

    def deal(self):

        '''
        Return a random card
        '''

        deck.shuffle_deck()
        dealt_card = random.choice(self.deck)
        return dealt_card


    def __str__(self):
        return str(self.deck)



# Hand Class
deck = Deck()
class Hand:

    '''
    Show current
    '''

    def __init__(self):
        self.hand = []


    def add_card(self):
        self.hand.append(deck.deal())

        return self.hand

    def __str__(self):

        return str(self.hand)


    def __len__(self):
        return len(self.hand)

    def hand_value(self):
        '''
        Show the value of the hand
        '''
        hand_alpha_list = []
        for val in self.hand:
            value_alpha = val.values()
            value_alpha = list(value_alpha)
            hand_alpha_list.append(value_alpha[0])

        # print(hand_alpha_list)
        # Initialize the total value
        total_value = 0

        # Iterate through the list to get rank
        for i_value in hand_alpha_list:
            if i_value == 'Two':
                value_num = 2
            elif i_value == 'Three':
                value_num = 3
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
                value_num = 11

            total_value += value_num

        return total_value



'''
# Test(1)
try:
    card = Card()
    print()
    print('Test One')
    print('Cards are: ',card)
except:
    print('There is an error in initializing cards')

# Test(2)
try:
    deck = Deck()
    print()
    print('Test Two')
    print('Deck is: ',deck)
    print('.....')
    print('Dealt Card: ',deck.deal())
except:
    print('There is an error in initializing the deck of cards')

# Test(3)
try:
    hand = Hand()
    print()
    print('Test Three')
    print('First Hand: ',hand.add_card())
    print('Second Hand: ',hand.add_card())
    print('All: ',hand)

    print('Current Value: ',hand.hand_value())
except:
    print('There is an error')
'''

# Game Logic
def game_logic():

    try:

        # Start Game
        print('...WELCOME TO BLACKJACK...')
        print('XXX...XXX...XXX...XXX...XXX')
        print()
        # Dealer Entry
        dealer = Dealer()
        # Player Entry
        player = Player()
        player.bet_stake()
        # Deck Initialization
        deck = Deck()

        # Create Individual Hands
        player_hand = Hand()
        dealer_hand = Hand()

        # Give player two cards
        player_hand.add_card()
        player_hand.add_card()
        print()
        print('{} Hand: '.format(player),player_hand)
        print('{} Points: '.format(player),player_hand.hand_value())

        # Give dealer two cards
        dealer_hand.add_card()
        dealer_hand.add_card()
        print()
        print('Dealer Hand: ',dealer_hand)
        print('Dealer Points: ',dealer_hand.hand_value())

    except:

        # Print any Errors and Exceptions
        print('There is an Error')

    finally:

        while player_hand.hand_value() < 21 and dealer_hand.hand_value() < 21:
            hit_or_stand = input('Hit(H) or Stand(S): ')
            if hit_or_stand.lower() == 'h':
                player_hand.add_card()
                print()
                print('{} Hand: '.format(player),player_hand)
                print('{} Points: '.format(player),player_hand.hand_value())
                print()
                print('Dealer Hand: ',dealer_hand)
                print('Dealer Points: ',dealer_hand.hand_value())
                continue
            else:
                dealer_hand.add_card()
                print()
                print('{} Hand: '.format(player),player_hand)
                print('{} Points: '.format(player),player_hand.hand_value())
                print()
                print('Dealer Hand: ',dealer_hand)
                print('Dealer Points: ',dealer_hand.hand_value())
                continue


        if player_hand.hand_value() < dealer_hand.hand_value():
            print()
            player.lose_bet()
        elif player_hand.hand_value() > dealer_hand.hand_value():
            print()
            player.win_stake()
        else:
            pass


        rematch = input('Do you want a rematch? Yes(Y) or No(N): ')
        if rematch.lower() == 'y':
            game_logic()
        else:
            print('GAME OVER')



game_logic()
