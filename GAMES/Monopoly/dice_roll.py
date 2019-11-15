'''
A dice rolling simulator, with the option of adding -
upto 6 different die
'''
import random
def roll_die(number=2):
    '''
    where the magic happens
    '''
    # define face values
    face_values = [1, 2, 3, 4, 5, 6]
    # save outcomes in a list
    outcomes_list = []

    # define a placeholder value for while loop
    placeholder_boolean = True

    while placeholder_boolean:
        try:
            number = int(number)
        except ValueError:
            print('Invalid entry. Please enter a number')
            break
        else:
            if number > 6:
                print()
                print('Maximum number of dice available is 6')
                break
            elif number < 1:
                print()
                print('Minimum number of die is 1')
                break
            else:
                # shuffle numbers for a random result
                random.shuffle(face_values)
                # Iterate to add values to outcomes_list
                for i in range(1, number+1):
                    outcomes_list.append(face_values.pop())
                # break out of loop
                placeholder_boolean = False

    return outcomes_list

# Program Logic
def start_roll():
    total_val = 0
    values = roll_die()
    if len(values) == 0:
        print('...NO OUTCOMES...')
    else:
        print()
        print('...DIE OUTCOMES...')
        for val in values:
            print('Dice:{}\tValue:{}'.format(values.index(val), val))
            print('................')
            total_val += val
    return total_val
