def guessing_game():
    print('XXX.....GUESSING GAME.....XXX')
    print()
    print('XXX.....RULES.....XXX')
    print("1. If a player's guess is less than 1 or greater than 100, say 'OUT OF BOUNDS'")
    print("2. On a player's first turn, if their guess is within \n    -10 of the number, return 'WARM!' \n    -further than 10 away from the number, return 'COLD!'")
    print("3. On all subsequent turns, if a guess is \n    -closer to the number than the previous guess return 'WARMER!'\n    -farther from the number than the previous guess, return 'COLDER!'")
    print("4. When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!")
    print()
    print("LET'S DO THIS")
    print()
    
    # Initialize tries
    tries = 0
    # Module for generating a random number 
    import random
    random_number = random.randint(1,100)
    # List to store player guesses
    guess_list = [0]
    
    while True:
        random_guess = input('I have a number in mind in the range of 1-100. Guess the number: ')
        random_guess = int(random_guess)
        guess_list.append(random_guess)
        tries += 1
        
        
        absolute_value = abs(random_guess - random_number)
        second_absolute_value = abs(guess_list[-2] - guess_list[-1])
        
        if tries == 1:
            if random_guess < 1 or random_guess > 100:
                print ('OUT OF BOUNDS')
            else:
                if random_number in guess_list:
                    print('CORRECT. It took you',tries,'tries')
                    break
                else:
                    if absolute_value <= 10:
                        print('WARM')
                    elif absolute_value > 10:
                        print('COLD')
        else:
            if random_guess < 1 or random_guess > 100:
                print ('OUT OF BOUNDS')
            else:
                if random_number in guess_list:
                    print('CORRECT. It took you',tries,'tries')
                    break
                else:
                    if second_absolute_value <= absolute_value:
                        print('COLDER')
                    else:
                        print('WARMER')





guessing_game()
        
        
            