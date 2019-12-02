class Player():
    '''
    Attributes
    1) Money
    2) ID
    3) Property

    Players can be 2 to 6
    '''
    def __init__(self, player_name, player_money=1500, player_assets=[]):
        self.player_name = player_name
        self.player_money = player_money
        self.player_assets = player_assets

    def __str__(self):
        print('...YOUR DETAILS...')
        return 'NAME: {}\nBALANCE: {}\nASSETS: {}'.format(
        self.player_name, self.player_money, self.player_assets
        )

    def buy_property(self, game_property):
        # Check if property is owned by bank
        # Property can only be bought if owned by bank and not another play in the game
        if game_property.owned == 'BANK':
            # Request to buy property
            property_purchase = input('Do you want to buy this property? (Y or N)')
            if property_purchase.lower() == 'y':
                # Check if player has enough money to buy property
                if self.player_money >= game_property.value:
                    # Change owned from BANK to PLAYER NAME
                    game_property.owned = self.player_name
                    # Deduct player money
                    self.player_money -= game_property.value
                    print()
                    print('PURCHASE ANNOUNCEMENT')
                    print('NEW OWNER: {}\nASSET: {}'.format(self.player_name, game_property))
                    self.player_assets.append(game_property)
                    print()
                    print('UPDATED ASSET LIST')
                    for assets in self.player_assets:
                        print(assets)
                else:
                    print('You do not have enough funds to complete this purchase')
            else:
                print('Maybe next time')
        else:
            print('This property is owned by someone else')

    def sell_property(self, game_property):
        # Check if player owns property
        if game_property.owned == self.player_name:
            # Request for sale
            property_sale = input('Do you want to sell this property? (Y or N)')
            if property_sale.lower() == 'y':
                # change owned back to BANK from PLAYER NAME
                game_property.owned = 'BANK'
                # add money to player
                self.player_money += game_property.value
                print()
                print('SALE ANNOUNCEMENT')
                print('NAME: {}\nASSET: {}'.format(self.player_name, game_property))
                self.player_assets.pop()
                print()
                print('UPDATED ASSET LIST')
                for assets in self.player_assets:
                    print(assets)
            else:
                print('This property is still yours')
        else:
            print('This property is not yours')
