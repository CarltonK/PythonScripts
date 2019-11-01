#!/usr/bin/env python
# coding: utf-8

# In[47]:


def game_intro():
    
    # Introduce the game
    print('...TIC...TAC...TOE...')
    print()
    
    # Two count while loop to get 2 player names
    count = 2
    # List to store player names
    player_list = []
    # Dict to store names and preffered letter (X or O)
    player_dict = {}
    while count > 0:
        player_name = input('Enter player name: ')
        player_list.append(player_name.title())
        count -= 1
          
    print()
    
    # Players choose preferred marker
    while player_list:
        player_choice = input('{} choose your preffered option (X or O): '.format(player_list[0]))
        if player_choice.upper() == 'X':
            player_dict = {player_list[0]:player_choice.upper(),player_list[1]:'O'}
            break
        elif player_choice.upper() == 'O':
            player_dict = {player_list[0]:player_choice.upper(),player_list[1]:'X'}
            break
        else:
            print('Please pick either "X" or "O"')
            continue
            
    print()
    player_list.append(player_dict)
    return player_list
    


# In[84]:



from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('.TIC.TAC.TOE.')
    print('..X.O.X.O..')
    print('GAME BOARD')
    print()
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


# In[85]:


def place_marker(board,marker,position):
    position = int(position)
    board[position] = marker


# In[86]:


def check_winner(board,marker):
    # List containing indexes of all winning combinations
    top_row = [1,2,3]
    mid_row = [4,5,6]
    bot_row = [7,8,9]
    left_col = [1,4,7]
    mid_col = [2,5,8]
    right_col = [3,6,9]
    principal_diag = [1,5,9]
    other_diag = [3,5,7]
    
    
    
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
           (board[4] == marker and board[5] == marker and board[6] == marker) or
           (board[7] == marker and board[8] == marker and board[9] == marker) or
           (board[1] == marker and board[4] == marker and board[7] == marker) or
           (board[2] == marker and board[5] == marker and board[8] == marker) or
           (board[3] == marker and board[6] == marker and board[9] == marker) or
           (board[1] == marker and board[5] == marker and board[9] == marker) or
           (board[3] == marker and board[5] == marker and board[7] == marker))


# In[87]:


# Check if there is an empty space in the board
def space_checker(board,position):
    if board[position] == '' or board[position] == ' ':
        return True
    else:
        return False
    
    
    


# In[88]:


def full_board(board):
    for i in range(1,10):
        if space_checker(board,i):
            return False
        
    return True


# In[89]:


def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_checker(board,position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[90]:


def replay():
    reply = input('Do you want to play the game again. Enter ("Y" or "N"): ')
    if reply.lower() == 'y':
        return True
    else:
        return False


# In[93]:


while True:
    player_dict = game_intro()
    game_board = [' '] * 10
    # Print Initial board
    

    
    # Player Particulars
    p1_name = player_dict[0]
    p1_marker = player_dict[2][p1_name]
    p2_name  = player_dict[1]
    p2_marker = player_dict[2][p2_name]
    
    print('Welcome to the game',p1_name,'and',p2_name)
    print(p1_name,'takes',p1_marker,'and',p2_name,'takes',p2_marker)
    
    play_game = input('Are you ready to play? Enter ("Y" or "N"): ')
    
    if play_game.lower() == 'y':
        print(p1_name,'goes first')
        game_on = True
    else:
        print('Be Serious')
        game_on = False
        
    turn = p1_name
    
    while game_on:
        
        # Player 1 Starts
        if turn == p1_name:
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board,p1_marker,position)
            
            if check_winner(game_board,p1_marker):
                display_board(game_board)
                print('Congratulations',p1_name,'you have won the game')
                game_on = False
            else:
                 if full_board(game_board):
                    display_board(game_board)
                    print('The game is a draw!')
                    break
                 else:
                    turn = p2_name
        else:
            # Player2's turn.
            
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, p2_marker, position)

            if check_winner(game_board, p2_marker):
                display_board(game_board)
                print(p2_name,'has won!')
                game_on = False
            else:
                if full_board(game_board):
                    display_board(game_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = p1_name
      
    
    if replay():
        continue
    else:
        print('GAME OVER')
        break
    

