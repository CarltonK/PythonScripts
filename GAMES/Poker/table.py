'''
This class represents the list of cards on the table
'''
class Table():

    def __init__(self):
        self.table_top = []

    def add_cards(self, card={}):
        '''
        Add a card to list of cards on the table
        '''
        self.table_top.append(card)

    def __str__(self):
        print('TABLE\n.....')
        return str(self.table_top)

'''
t = Table()
t.add_cards({'Hearts':'Two'})
t.add_cards({'Hearts':'Three'})
t.add_cards({'Hearts':'Four'})
t.add_cards({'Hearts':'Five'})
print(t)
'''
