class Player():
    '''
    Attributes
    1) Money
    2) ID
    3) Property

    Players can be 2 to 6
    '''
    def __init__(self, player_name, player_money=1500, player_property=[], player_value=0):
        self.player_name = player_name
        self.player_money = player_money
        self.player_property = player_property
        self.player_value = player_value

    def __str__(self):
        print()
        return 'NAME: {}\nBALANCE: {}\nPROPERTY: {}\nVALUE: {}'.format(
        self.player_name, self.player_money, self.player_property,
        self.player_grandvalue()
        )

    def buy_property(self, game_property):
        print()
        print('NAME: {}\nPROPERTY PURCHASE: {}'.format(self.player_name, game_property))
        self.player_property.append(game_property)
        print('UPDATED PROPERTY LIST: {}'.format(self.player_property))

    def sell_property(self, game_property):
        print()
        print('NAME: {}\nPROPERTY SALE: {}'.format(self.player_name, game_property))
        self.player_property.remove(game_property)
        print('UPDATED PROPERTY LIST: {}'.format(self.player_property))

    def player_grandvalue(self):
        self.player_value += self.player_money
        if len(self.player_property) == 0:
            pass
        else:
            for props in player_property:
                for val in list(props.values()):
                    self.player_value += val

        return self.player_value
