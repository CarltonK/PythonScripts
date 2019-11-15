'''
Simple 'Guess the Word' game
Supporting modules are wordlist and random
Wordlist for grabbing words, random for shuffling words for a randomized result
'''

import random
import wordlist


# List to store returned words
WORDS_LIST = []

# Word processing
print(' HANGMAN ')
print('Loading...')
def word_grabber():
    '''
    Generate words using wordlist
    Shuffle list to get one word
    '''
    word_generator = wordlist.Generator('charset')
    for single_word in word_generator.generate(5, 7):
        WORDS_LIST.append(single_word)

    # Shuffle
    random.shuffle(WORDS_LIST)

    return WORDS_LIST.pop()

def hangman_game(correct_value):
    '''
    Administrator enters correct value first (when comment below is removed,
    otherwise game is automatic)
    Player enters guess(letter)
    Limit number of guesses
    Notify player of remaining guesses
    '''

    # Remove below comment to make game manual
    # correct_value = input('Enter the letter you want the player to guess? ')
    print('The word has {} letters'.format(len(correct_value)))

    #set a counter equal to length of word
    running_count = len(correct_value)
    try:


        while running_count > 0:
            # Solicit player input
            player_guess = input('Guess a letter: ')
            valid_value = player_guess[0]

            if valid_value.isalpha() == False:
                print('Invalid entry...Please enter a letter')
            else:
                valid_value = valid_value.lower()

            # Assign returned value to a variable
            # correct_value = 'hawks'
            temp_val = '* ' * len(correct_value)
            temporary_value = temp_val.split()


            if valid_value in correct_value:

                print()
                print('Your letter appears {} times'.format(correct_value.count(valid_value)))
                temporary_value[correct_value.index(valid_value)] = valid_value

            else:
                print()
                print('{} is not in the word'.format(valid_value))

            running_count -= 1


            print('Running word: {}'.format(temporary_value))
            print('You have {} remaining tries'.format(running_count))
            print()
    except:
        print('There is an error')

    finally:
        if running_count == 0:
            print('GAME OVER')
            print('The word was {}'.format(correct_value))
        else:
            pass



# Execution
hangman_game(word_grabber())
