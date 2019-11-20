'''
This is the main file
'''
from card import Card
from deck import Deck
from poker_player import Player


players_list = []
def poker_game():
    print('...WELCOME TO POKER...')
    # Indicates that max number of players is 5
    while len(players_list) < 5:
        player_name = input('Enter your name: ')
        players_list.append(player_name)

    # Iterate through players list to assign players
    for i in players_list:
        single_player = Player(i)
        print(single_player)

    # Start Game
    game_on = True
    while game_on:
        game_on = False


if __name__ == '__main__':
    poker_game()
