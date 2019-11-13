'''
Account class as Base class
'''
class Account():

    def __init__(self, acc_num, balance=0):
        self.acc_num = acc_num
        self.balance = balance
        self.open_account()

    def open_account(self):
        '''
        Open a bank account to proceed
        '''
        print('WELCOME TO CARLTON BANK')
        while True:
            try:
                request = int(input('Minimum deposit fee is 1000.\nHow much do you want to deposit? '))
            except ValueError:
                print('Invalid entry. Please enter a number')
            else:
                if request < 1000:
                    print('Minimum amount is 1000')
                else:
                    self.balance += request
                    print()
                    print('...ACCOUNT DETAILS...')
                    print('Account Number: {}\nAccount Balance: {}'.format(self.acc_num, self.balance))
                    break

    def deposit_funds(self):
        while True:
            try:
                deposit = int(input('How much do you want to deposit? '))
            except ValueError:
                print('Invalid entry. Please enter a number')
            else:
                self.balance += deposit
                print()
                print('...ACCOUNT DETAILS...')
                print('Account Number: {}\nAccount Balance: {}'.format(self.acc_num, self.balance))
                break

    def withdraw_funds(self):
        while True:
            try:
                withdraw = int(input('How much do you want to withdraw? '))
            except ValueError:
                print('Invalid entry. Please enter a number.')
            else:
                if withdraw > self.balance:
                    print('...ERROR...\nINSUFFICIENT FUNDS\nAvailable balance: {}'.format(self.balance))
                else:
                    self.balance -= withdraw
                    print()
                    print('...ACCOUNT DETAILS...')
                    print('Account Number: {}\nAccount Balance: {}'.format(self.acc_num, self.balance))
                    break

    def __str__(self):
        return 'Account Number: {}\nAccount Balance: {}'.format(self.acc_num, self.balance)

    '''
    def __del__(self):
        choice = input('Do you want to close your account? ')
        if choice[0].lower() == 'y':
            del(self)
            print('Account {} has been closed'.format(self.acc_num))
        else:
            print('Account not deleted')
    '''


def generate_id():
    '''
    Generate random characters to be set as Account Number
    '''
    # Random selection
    import random

    lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
                  'n','o','p','q','r','s','t','u','v','w','x','y','z']

    upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                  'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    number_char = ['0','1','2','3','4','5','6','7','8','9']

    vi_length = 10

    vi_identifier = ''

    while len(vi_identifier) < vi_length:
        # Shuffle respective lists
        random.shuffle(lower_case)
        random.shuffle(upper_case)
        random.shuffle(number_char)

        # Concatenate results to existing vi_identifier
        vi_identifier += upper_case.pop()
        vi_identifier += lower_case.pop()
        vi_identifier += number_char.pop()

    return vi_identifier


'''
Savings account
'''
class SavingsAccount(Account):

    def __init__(self, acc_num = generate_id(), balance = 0):
        super().__init__(acc_num, balance)

    def open_account(self):
        '''
        Open a savings account to proceed
        '''
        print('WELCOME TO CARLTON BANK')
        while True:
            try:
                request = int(input('Minimum deposit fee is 1000.\nHow much do you want to deposit? '))
            except ValueError:
                print('Invalid entry. Please enter a number')
            else:
                if request < 1000:
                    print('Minimum amount is 1000')
                else:
                    self.balance += request
                    break

    def __str__(self):
        return '...SAVINGS ACCOUNT...\n{}'.format(Account.__str__(self))



'''
Current Account
'''
class CurrentAccount(Account):
    def __init__(self, acc_num = generate_id(), balance = 0):
        super().__init__(acc_num, balance)

    def open_account(self):
        '''
        Open a current account to proceed
        '''
        print('WELCOME TO CARLTON BANK')
        while True:
            try:
                request = int(input('Minimum deposit fee is 1000.\nHow much do you want to deposit? '))
            except ValueError:
                print('Invalid entry. Please enter a number')
            else:
                if request < 1000:
                    print('Minimum amount is 1000')
                else:
                    self.balance += request
                    break

    def __str__(self):
        return '...CURRENT ACCOUNT...\n{}'.format(Account.__str__(self))

save = SavingsAccount()
print(save)

curr = CurrentAccount()
print(curr)

save.deposit_funds()
curr.withdraw_funds()
