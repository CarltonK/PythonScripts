'''
A password generator designed for flexibility
Includes lowercase and uppercase letters, numbers,
special characters and symbols
Minimum length of password is 6
'''
import random
def password_generator(length=4):

    lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    number_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols_char = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '.', ',']

    user_password = ''

    placeholder_boolean = True
    while placeholder_boolean:

        user_length = input('Enter desired password length: ')


        try:
            length = int(user_length)
            if length > 40:
                print('Password is too long')
                continue
            else:
                pass

        except ValueError:
            print('Length should be a number')
            continue

        else:

            while len(user_password) < length:
                # Shuffle respective lists
                random.shuffle(lower_case)
                random.shuffle(upper_case)
                random.shuffle(number_char)
                random.shuffle(symbols_char)

                # Concatenate results to existing user password variable
                user_password += lower_case.pop()
                user_password += upper_case.pop()
                user_password += number_char.pop()
                user_password += symbols_char.pop()

        print('Your password is {}'.format(user_password))

        placeholder_boolean = False

# Execution
password_generator()
