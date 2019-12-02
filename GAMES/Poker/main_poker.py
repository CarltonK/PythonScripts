'''
This is the main file
'''
from card import Card
from deck import Deck
from poker_player import Player
from table import Table

players_list = []
print('...WELCOME TO POKER...')
# Indicates that max number of players is 5
while len(players_list) < 5:
    player_name = input('Enter your name: ')
    players_list.append(player_name)

# Initialize the deck
game_deck = Deck()
index = 0

# Iterate through players list to assign players
for i in players_list:
    player_hand = [game_deck.deal(), game_deck.deal(),
                   game_deck.deal(), game_deck.deal()]
    single_player = Player(i, player_hand)
    players_list[index] = single_player
    index += 1
    print(single_player)


def poker_game():
    # Start Game
    print()
    print('...GAME ON...')
    game_on = True
    while game_on:
        game_table = Table()
        for i in players_list:
            print(i)
            p_choice = input('Drop (D) or Pick (P)? ')
            if p_choice[0].lower() == 'd':
                # Drop card and add to the table
                game_table.add_cards(i.drop_card())
                # Drop card
                #i.drop_card()
            elif p_choice[0].lower() == 'p':
                # Pick card
                i.pick_card(game_deck.deal())
            else:
                raise ValueError('Cheza game poa. Wacha ufala')

            print(game_table)

        game_on = False


if __name__ == '__main__':
    poker_game()
