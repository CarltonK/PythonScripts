'''
This class represents stations
'''
class Station():

    def __init__(self, stat={}, owned=False):
        self.stat = stat
        self.owned = owned

    def __str__(self):
        entire_stat = []

        if self.owned == False:
            self.owned = 'BANK'
        else:
            pass

        entire_stat.append(self.stat)
        entire_stat.append(self.owned)

        return 'STATION: {}\nOWNER: {}'.format(
                entire_stat[0], entire_stat[1])
            
