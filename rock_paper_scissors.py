def rps_game(p1_name,p2_name):
    print()
    print('...ROCK.PAPER.SCISSORS...')
    print('Welcome to the game',p1_name.title(),'and',p2_name.title())
    print()
    tries = 3

    while tries >= 1:

        p1_answer = input('Enter either "rock", "paper" or "scissors": ')
        p2_answer = input('Enter either "rock", "paper" or "scissors": ')
        combined_answer = p1_answer.lower() + p2_answer.lower()

        if tries <= 0:
            print('...GAME OVER...')
            break
        else:
            if p1_answer.lower() == p2_answer.lower():
                print()
                tries -= 1
                print('It\'s a tie')
            elif 'rock' in combined_answer and 'paper' in combined_answer:
                print()
                print('Paper covers rock')
                if 'paper' in p1_answer.lower():
                    tries -= 1
                    print('You win',p1_name)
                elif 'paper' in p2_answer.lower():
                    tries -= 1
                    print('You win',p2_name)
                break
            elif 'rock' in combined_answer and 'scissors' in combined_answer:
                print()
                tries -= 1
                print('Rock crushes scissors')
                if 'rock' in p1_answer.lower():
                    tries -= 1
                    print('You win',p1_name)
                elif 'rock' in p2_answer.lower():
                    tries -= 1
                    print('You win',p2_name)
                break
            elif 'paper' in combined_answer and 'scissors' in combined_answer:
                print()
                print('Scissors cuts paper')
                tries -= 1
                if 'scissors' in p1_answer.lower():
                    tries -= 1
                    print('You win',p1_name)
                elif 'scissors' in p2_answer.lower():
                    tries -= 1
                    print('You win',p2_name)
                break
            else:
                print()
                tries -= 1
                print('Please enter a valid answer')


p1 = input('Enter your name: ')
p2 = input('Enter your name: ')
rps_game(p1,p2)
