'''
Binary Search Algorithm
Check whether a number is contained in a list, by halving the list, indexing
the list and comparing the searched value with the value at the indexed
position
Process continues until number is found or until subarray is 0
'''# Import Random Module
import random

# Create a placeholder list, set it to empty initially
number_list = []

# Populate the list with random integers from 0-100
# While loop to iterate through the random numbers generated
while len(number_list) < 100:
    number_list.append(random.randrange(0, 100, 2))


# Remove duplicates. Convert the list to a set and back to a list again
number_list = set(number_list)
number_list = list(number_list)
# Get user input
search_boolean = True
while search_boolean:
    try:
        search_number = int(input('Enter a number (0-100): '))
    except ValueError:
        print('Invalid Entry. Please Enter a Number')
    else:
        if search_number in range(0, 101):
            search_boolean = False
        else:
            print('Enter a number that falls between 0-100')
            continue


def search_logic(number, numlist):
    '''
    Determine the length of the list
    Halve the list to get a specific index, call it mid_point
    Index the list with mid_point to get the specific value, call it middle_value
    Compare the user input with the middle value
    End the search if True else continue until subarray = 0 or value is found
    Keep a counter of steps taken [Optional]
    '''

    game_in_progress = True
    steps = 0
    while game_in_progress:

        # Constant reminder of the value we are looking for
        print('{} is the number we are looking for'.format(search_number))
        middle_point = int(len(numlist) / 2)
        middle_value = numlist[middle_point]
        print('The middle value is: {}'.format(middle_value))
        print()


        first_half = numlist[:middle_point]
        second_half = numlist[middle_point:]
        print('First Half: {}'.format(first_half))
        print('Second Half: {}'.format(second_half))

        if number == middle_value:
            print('Value Found')
            game_in_progress = False
        elif len(first_half) == 0 or len(second_half) == 0:
            print('{} is not in this list'.format(number))
            game_in_progress = False
        else:
            if number > middle_value:
                numlist = second_half
            elif number < middle_value:
                numlist = first_half
            else:
                continue

            steps += 1

    print('You took {} steps'.format(steps))


print('Initial List: {}'.format(number_list))
search_logic(search_number, number_list)
