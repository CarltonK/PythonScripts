'''
This is a basic calculator
Operations are addition, subtraction, multiplication and division
'''
def calculator(*args):
    total = 0
    place_boolean = True
    while place_boolean:

        try:
            operation = input('Enter desired operation (+, -, *, /): ')
        except ValueError:
            print('Invalid operator. Please try again')
        else:
            operators = ['+', '-', '*', '/']
            if operation not in operators:
                print('Invalid operator. Please try again')
            else:
                if operation == '+':
                    for val in args:
                        total += val
                elif operation == '-':
                    for val in args:
                        total -= val
                elif operation == '*':
                    total = 1
                    for val in args:
                        total *= val
                elif operation == '/':
                    total = 1
                    for val in args:
                        total /= val
                else:
                    print('Invalid operator. Please try again')

                place_boolean = False
    print('Total:    {}\nOperator: {}'.format(total, operation))


calculator(1, 2, 3, 4, 5)
