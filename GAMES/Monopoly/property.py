class Property():
    '''
    Single Property
    prop = {'PROPERTY NAME':PROPERTY VALUE}
    houses = houses erected in property
    hotels = hotels erected in property
    '''

    def __init__(self, prop={}, houses=0, hotels=0):
        self.houses = houses
        self.hotels = hotels
        self.prop = prop

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
        
