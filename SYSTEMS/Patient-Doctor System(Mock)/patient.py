'''
This module contains all relevant patient information
'''
class Patient():

    def __init__(self, name, age, height, weight, history=[]):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.history = history
        self.bmi = self.get_bmi()

    def make_appointment(self, time):
        request = input('Would you like to make an appointment ? (Y or N): ')
        if request[0].lower() == 'y':
            print('NAME: {}\nTIME: {}'.format(self.name, time))
        elif request[0].lower() == 'n':
            print('Maybe next time')
        else:
            print('We take is as a NO')

    def get_bmi(self):
        self.height = (self.height)/100
        bmi = self.weight/(self.height ** 2)
        return bmi

    def __str__(self):
        return 'NAME: {}\nAGE: {}\nBMI: {}'.format(
                self.name, self.age, self.bmi)

pat = Patient('Mark', 23, 177, 83)
print(pat)
