'''
This class represents utilities
'''
class Utility():

    def __init__(self, util={}, owned=False):
        self.util = util
        self.owned = owned

    def __str__(self):
        entire_util = []

        if self.owned == False:
            self.owned = 'BANK'
        else:
            pass

        entire_util.append(self.util)
        entire_util.append(self.owned)

        return 'UTILITY: {}\nOWNER: {}'.format(
                entire_util[0], entire_util[1])
