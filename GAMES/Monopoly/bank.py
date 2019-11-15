class Bank():
    '''
    Besides the Bank’s money, the Bank holds the Title Deed cards and
    houses and hotels prior to purchase and use by the players.

    The Bank pays salaries and bonuses. It sells and auctions properties and hands out
    their proper Title Deed cards; it sells houses and hotels to the players and loans
    money when required on mortgages.

    The Bank collects all taxes, fines, loans and interest, and the price of all properties
    which it sells and auctions.

    The Bank never “goes broke.” If the Bank runs out of money, the Banker may issue
    as much more as may be needed by writing on any ordinary paper.
    '''
    def __init__(self, total_money=20580, houses=32, hotels=12, properties=[]):
        self.total_money = total_money
        self.houses = houses
        self.hotels = hotels
        self.properties = properties

    def credit_money(self, cred_sum=0):
        '''
        Receive money from players, in the form of fines or taxes
        '''
        cred_sum = int(input('Credit Amount: '))
        self.total_money += cred_sum
        return cred_sum

    def debit_money(self, deb_sum=0):
        '''
        Give money to players in the form of gifts
        '''
        deb_sum = int(input('Debit Amount: '))
        self.total_money -= deb_sum
        return deb_sum

    def game_properties(self):
        pass
