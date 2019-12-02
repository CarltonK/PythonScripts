'''
An armstrong number is a number which is an addition resultant of individual numbers,
raised to the power of the length of the number
Single digits are armstrong numbers
'''

def armstrong_checker(number):
    '''
    Convert number to string because an integer is neither iterable nor subscriptable
    '''
    # Change number to string to get length
    number = str(number)
    # Get the length of the number
    number_length = len(number)
    # Define a placeholder_value
    running_total = 0
    # Iterate through all numbers raising them to number_length as the power
    for digit in number:
        # Change digit to integer
        digit = int(digit)
        running_total += (digit ** number_length)

    if running_total == int(number):
        print('{} is an armstrong number'.format(number))
    else:
        print('{} is NOT an armstrong number'.format(number))


# Logic
PLACEHOLDER_BOOLEAN = True
while PLACEHOLDER_BOOLEAN:
    try:
        number = int(input('Enter an armstrong number: '))
    except ValueError:
        print('Please enter a valid number')
    else:
        armstrong_checker(number)
        PLACEHOLDER_BOOLEAN = False
