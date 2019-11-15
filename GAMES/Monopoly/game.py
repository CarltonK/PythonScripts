'''
Game Logic
'''
# Import necessary modules
import auxillary_cards
import bank
import dice_roll
import player
import property
import station
import utility
import game_board

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
print('Let\'s get the names of players')
count = 0
while count < num_players:
    p_name = input('What is your name? ')
    game_players.append(p_name.upper())
    count += 1

# Print players who are in the game
print('Players: {}'.format(game_players))

# Assign players unique numbers
for play in game_players:
    playboy = player.Player(play)
    print(playboy)

# Take turns playing
p_index = 0
turn = game_players[p_index]
print()
print('{} goes first'.format(turn))

if turn == game_players[0]:
    steps = dice_roll.start_roll()
    print('Move {} steps'.format(steps))
