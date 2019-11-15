class Property():
    '''
    Single Property
    prop = {'PROPERTY NAME':PROPERTY VALUE}
    houses = houses erected in property
    hotels = hotels erected in property
    Entire property is enclosed in a list
    E.g
    [prop, houses, hotels, owner]
    '''

    def __init__(self, prop={}, houses=0, hotels=0, owned=False):
        self.houses = houses
        self.hotels = hotels
        self.prop = prop
        self.owned = owned

    def erect_hotels(self):
        house_request = input('Do you want to build a house (Y or N)? ')
        if house_request[0].lower() == 'y':
            self.houses = 1
        else:
            pass

    def erect_houses(self):
        if self.houses == 4:
            hotel_request = input('Do you want to build a hotel (Y or N)? ')
            if hotel_request[0].lower() == 'y':
                self.houses -= 4
                self.hotels += 1
            else:
                pass

    def __str__(self):
        entire_property = []

        if self.owned == False:
            self.owned = 'BANK'
        else:
            pass

        entire_property.append(self.prop)
        entire_property.append(self.houses)
        entire_property.append(self.hotels)
        entire_property.append(self.owned)

        return 'PROPERTY: {}\nHOUSES: {}\nHOTELS: {}\nOWNER: {}'.format(
                entire_property[0], entire_property[1],
                entire_property[2], entire_property[3])
