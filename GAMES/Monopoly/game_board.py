'''
This class represents the game board
'''

# Import necessary modules
import single_property


class Board():

    def __init__(self, spaces=[], chance=[], community=[]):
        self.spaces = spaces
        self.chance = chance
        self.community = community

        # Define Properties
        old_kent = single_property.Property({'OLD KENT ROAD':60})
        whitechapel = single_property.Property({'WHITECHAPEL ROAD':60})
        angel = single_property.Property({'ANGEL ISLINGTON':100})
        euston = single_property.Property({'EUSTON ROAD':100})
        pentoville = single_property.Property({'PENTOVILLE ROAD':120})
        pall = single_property.Property({'PALL MALL':140})
        whitehall = single_property.Property({'WHITEHALL':140})
        northumber = single_property.Property({'NORTHUMBERLAND':160})
        bow = single_property.Property({'BOW STREET':180})
        marl = single_property.Property({'MARLBOUROUGH STREET':180})
        vine = single_property.Property({'VINE STREET':200})
        strand = single_property.Property({'STRAND':220})
        fleet = single_property.Property({'FLEET STREET':220})
        trafalgar = single_property.Property({'TRAFALGAR SQUARE':240})
        leicester = single_property.Property({'LEICESTER SQUARE':260})
        coventry = single_property.Property({'COVENTRY STREET':260})
        piccadilly = single_property.Property({'PICCADILLY':280})
        regent = single_property.Property({'REGENT STREET':300})
        oxford = single_property.Property({'OXFORD STREET':300})
        bond = single_property.Property({'BOND STREET':320})
        parklane = single_property.Property({'PARK LANE':350})
        mayfair = single_property.Property({'MAYFAIR':400})

        # Define stations
        kingscross = single_property.Property({'KINGS CROSS STATION':200})
        maryle = single_property.Property({'MARYLEBONE STATION':200})
        fenchurch = single_property.Property({'FENCHURCH STATION':200})
        liverpool = single_property.Property({'LIVERPOOL STREET STATION':200})

        # Define Utilities
        water = single_property.Property({'WATER WORKS':150})
        elec = single_property.Property({'ELECTRIC COMPANY':150})

        # Fill Board
        self.spaces.append('GO')
        self.spaces.append(old_kent)
        self.spaces.append('COMMUNITY CHEST')
        self.spaces.append(whitechapel)
        self.spaces.append({'INCOME TAX':100})
        self.spaces.append(maryle)
        self.spaces.append(angel)
        self.spaces.append('CHANCE')
        self.spaces.append(euston)
        self.spaces.append(pentoville)
        self.spaces.append('JAIL')
        self.spaces.append(pall)
        self.spaces.append(elec)
        self.spaces.append(whitehall)
        self.spaces.append(northumber)
        self.spaces.append(fenchurch)
        self.spaces.append(bow)
        self.spaces.append('COMMUNITY CHEST')
        self.spaces.append(marl)
        self.spaces.append(vine)
        self.spaces.append('FREE PARKING')
        self.spaces.append(strand)
        self.spaces.append('CHANCE')
        self.spaces.append(fleet)
        self.spaces.append(trafalgar)
        self.spaces.append(kingscross)
        self.spaces.append(leicester)
        self.spaces.append(coventry)
        self.spaces.append(water)
        self.spaces.append(piccadilly)
        self.spaces.append('GO TO JAIL')
        self.spaces.append(regent)
        self.spaces.append(oxford)
        self.spaces.append('COMMUNITY CHEST')
        self.spaces.append(bond)
        self.spaces.append(liverpool)
        self.spaces.append('CHANCE')
        self.spaces.append(parklane)
        self.spaces.append({'SUPER TAX':200})
        self.spaces.append(mayfair)



    def chances(self):
        self.chance = ['Advance to Go (Collect $200)',
                       'Advance to Illinois Ave — If you pass Go, collect $200',
                       'Advance to St. Charles Place – If you pass Go, collect $200',
                       'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.',
                       'Advance token to the nearest Railroad and pay owner twice the rental to which he/she {he} is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.',
                       'Bank pays you dividend of $50',
                       'Get Out of Jail Free',
                       'Go Back 3 Spaces',
                       'Go to Jail–Go directly to Jail–Do not pass Go, do not collect $200',
                       'Make general repairs on all your property–For each house pay $25–For each hotel $100',
                       'Pay poor tax of $15',
                       'Take a trip to Reading Railroad–If you pass Go, collect $200',
                       'Take a walk on the Boardwalk–Advance token to Boardwalk',
                       'You have been elected Chairman of the Board–Pay each player $50',
                       'Your building and loan matures—Collect $150',
                       'Your building and loan matures—Collect $150']

        return self.chance.pop()

    def communities(self):
        self.community = ['Advance to Go (Collect $200)',
                       'Bank error in your favor—Collect $200',
                       "Doctor's fee - Pay $50",
                       'From sale of stock you get $50',
                       'Get Out of Jail Free',
                       'Go to Jail–Go directly to jail–Do not pass Go–Do not collect $200',
                       'Grand Opera Night—Collect $50 from every player for opening night seats',
                       'Holiday Fund matures—Receive $100',
                       'Income tax refund–Collect $20',
                       'It is your birthday—Collect $10',
                       'Life insurance matures–Collect $100',
                       'Pay hospital fees of $100',
                       'Pay school fees of $150',
                       'Receive $25 consultancy fee',
                       'You are assessed for street repairs–$40 per house–$115 per hotel',
                       'You have won second prize in a beauty contest–Collect $10',
                       'You inherit $100']

        return self.community.pop()

    def display_board(self):
        # Iterate through board list
        for pos in self.spaces:
            print(pos)
            print()
