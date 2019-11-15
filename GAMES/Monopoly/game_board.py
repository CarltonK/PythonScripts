'''
This class represents the game board
'''
class Board():

    def __init__(self, spaces=[], props=[], stats=[], utils=[]):
        self.spaces = spaces
        self.props = props

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

        self.props = [old_kent, whitechapel, angel, euston, pentoville, pall,
                          whitehall, northumber, bow, marl, vine, strand, fleet,
                          trafalgar, leicester, coventry, piccadilly, regent,
                          oxford, bond, parklane, mayfair]
        return self.props

    def stat_definitions(self):
        kingscross = Station({'KINGS CROSS STATION':200})
        maryle = Station({'MARYLEBONE STATION':200})
        fenchurch = Station({'FENCHURCH STATION':200})
        liverpool = Station({'LIVERPOOL STREET STATION':200})

        self.stats = [kingscross, maryle, fenchurch, liverpool]

        return self.stats

    def util_definitions(self):
        water = Utility({'WATER WORKS':150})
        elec = Utility({'ELECTRIC COMPANY':150})

        self.utils = [elec, water]

        return self.utils

    def display_board(self):
        pass
