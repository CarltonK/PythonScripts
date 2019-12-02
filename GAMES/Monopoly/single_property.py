class Property():
    '''
    Single Property
    prop = {'PROPERTY NAME':PROPERTY VALUE}
    value = prop['PROPERTY NAME']
    houses = houses erected in property
    hotels = hotels erected in property
    Entire property is enclosed in a list
    E.g
    [prop, houses, hotels, owner]
    '''

    def __init__(self, details={}, value=0, houses=0, hotels=0, owned='BANK'):
        '''
        Actions - 1) Assign value in details{} to property.value
        '''
        # Assign value to key
        key_value = list(details.keys())
        # Assign key to property value
        value = details[key_value[0]]

        self.houses = houses
        self.hotels = hotels
        self.details = details
        self.owned = owned
        self.value = value


        '''
        TEST
        dic = {'OLD KENT ROAD':60}
        x = list(dic.keys())
        print(x[0])
        dic[x[0]]
        '''

    def erect_houses(self):
        house_request = input('Do you want to build a house (Y or N)? ')
        if house_request[0].lower() == 'y':
            self.houses += 1
        else:
            print('You do not want to buy a house. You might want to make a move soon. Bye for now')

    def erect_hotels(self):
        if self.houses == 4:
            hotel_request = input('Do you want to build a hotel (Y or N)? ')
            if hotel_request[0].lower() == 'y':
                self.houses -= 4
                self.hotels += 1
            else:
                print('You do not want to build a hotel. You might want to make a move soon. Bye for now')
        else:
            print('A hotel can only be built if you own four houses')

    def erect_structure(self):
        # Check if player owns the property
        if self.owned == True:

            erection_request = input()

    def __str__(self):

        return 'PROPERTY: {}\nHOUSES: {}\nHOTELS: {}\nOWNER: {}'.format(
                self.details, self.houses,
                self.hotels, self.owned)
