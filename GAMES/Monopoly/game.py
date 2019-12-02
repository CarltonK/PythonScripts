'''
Game Logic
'''

# Import necessary modules
import auxillary_cards
import bank
import dice_roll
import game_board
import player
import single_property

prop = single_property.Property
aux = auxillary_cards.AuxCards()

def check_position(space, p):

    if type(space) == prop:

        if space.owned == 'BANK':
            user_act = input('Choose an action ("r") to roll dice, ("b") to buy property, ("s") to stay')
            if user_act.lower() == 'b':
                space.owned = p
                p.buy_property(space)
            elif user_act.lower() == 'r':
                dice_roll.start_roll()
                p != p
            else:
                p != p
        else:
            user_act = input('Pay rent to {}'.format(player))


    elif type(space) == str:
        aux.chance_card()
    elif type(space) == str:
        aux.community_card()



print('...MONOPOLY...MONOPOLY...MONOPOLY')
print('.......WELCOME TO THE GAME.......')

# List to hold names of players
game_players = []

# Get number of players playing
while True:
    try:
        num_players = int(input('How many players are in (2-6)? '))
    except ValueError:
        print('Invalid entry. Please enter a number')
    else:
        if num_players < 2:
            print('Minimum number of players are 2')
        elif num_players > 6:
            print('Maximum number of players are 6')
        else:
            print('{} are playing'.format(num_players))
            break

# Get names of Players
# Keep a counter
print()
print('Enter the names of players')
count = 0
while count < num_players:
    p_name = input('What is your name? ')
    game_players.append(p_name.upper())
    count += 1

# Print players who are in the game
print('Players: {}'.format(game_players))
print('Let the game begin')

game_on = True
while game_on:
    for players in game_players:
        print('It is your turn {}'.format(players))
        board = game_board.Board()
        board.display_board()
        steps = dice_roll.start_roll()
        print('Move {} steps'.format(steps))
        print('PREVIOUS POSITION: {}\nCURRENT POSITION: {}'.format(board.spaces[0], board.spaces[steps]))
        check_position(board.spaces[steps], player.Player(players))

        game_on = False
