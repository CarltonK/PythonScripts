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
    def __init__(self, total_money=20580, houses=32, hotels=12, props=[], stats=[], utils=[]):
        self.total_money = total_money
        self.houses = houses
        self.hotels = hotels
        self.props = props
        self.stats = stats
        self.utils = utils

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

    def prop_definitions(self):
        old_kent = Property({'OLD KENT ROAD':60})
        whitechapel = Property({'WHITECHAPEL ROAD':60})
        angel = Property({'ANGEL ISLINGTON':100})
        euston = Property({'EUSTON ROAD':100})
        pentoville = Property({'PENTOVILLE ROAD':120})
        pall = Property({'PALL MALL':140})
        whitehall = Property({'WHITEHALL':140})
        northumber = Property({'NORTHUMBERLAND':160})
        bow = Property({'BOW STREET':180})
        marl = Property({'MARLBOUROUGH STREET':180})
        vine = Property({'VINE STREET':200})
        strand = Property({'STRAND':220})
        fleet = Property({'FLEET STREET':220})
        trafalgar = Property({'TRAFALGAR SQUARE':240})
        leicester = Property({'LEICESTER SQUARE':260})
        coventry = Property({'COVENTRY STREET':260})
        piccadilly = Property({'PICCADILLY':280})
        regent = Property({'REGENT STREET':300})
        oxford = Property({'OXFORD STREET':300})
        bond = Property({'BOND STREET':320})
        parklane = Property({'PARK LANE':350})
        mayfair = Property({'MAYFAIR':400})

        self.props.append(old_kent)
        self.props.append(whitechapel)
        self.props.append(angel)
        self.props.append(euston)
        self.props.append(pentoville)
        self.props.append(pall)
        self.props.append(whitehall)
        self.props.append(northumber)
        self.props.append(bow)
        self.props.append(marl)
        self.props.append(vine)
        self.props.append(strand)
        self.props.append(fleet)
        self.props.append(trafalgar)
        self.props.append(leicester)
        self.props.append(coventry)
        self.props.append(piccadilly)
        self.props.append(regent)
        self.props.append(oxford)
        self.props.append(bond)
        self.props.append(parklane)
        self.props.append(mayfair)

        return self.props

    def stat_definitions(self):
        kingscross = Station({'KINGS CROSS STATION':200})
        maryle = Station({'MARYLEBONE STATION':200})
        fenchurch = Station({'FENCHURCH STATION':200})
        liverpool = Station({'LIVERPOOL STREET STATION':200})

        self.stats.append(kingscross)
        self.stats.append(maryle)
        self.stats.append(fenchurch)
        self.stats.append(liverpool)

        return self.stats

    def util_definitions(self):
        water = Utility({'WATER WORKS':150})
        elec = Utility({'ELECTRIC COMPANY':150})

        self.utils.append(elec)
        self.utils.append(water)

        return self.utils
