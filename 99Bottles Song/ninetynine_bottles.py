'''
99 Bottles of Beer" is an anonymous folk song dating to the mid-20th century.
It is a traditional reverse counting song in both the United States and Canada.
It is popular to sing on road trips, as it has a very repetitive format,
which is easy to memorize and can take a long time when families sing.
In particular, the song is often sung by children on long school bus trips,
such as class field trips, or on Scout and/or Girl Guide outings.
'''
def ninety_nine_bottles():
    '''
    Makes use of for loop and in-built python range function
    '''
    # Number of bottles + 1
    number = 100
    for i in range(1, 100):

        if number == 2:
            print('{} bottles of beer on the wall, {} bottles of beer.'.format(number-1, number-1))
            print('Take one down, pass it around, no bottle of beer on the wall...')
        else:
            print('{} bottles of beer on the wall, {} bottles of beer.'.format(number-1, number-1))
            print('Take one down, pass it around, {} bottles of beer on the wall...'.format(number-2))
            print()

        number -= 1

ninety_nine_bottles()
