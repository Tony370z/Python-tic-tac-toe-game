from IPython.display import clear_output
from random import randint

def display_board(board):
    clear_output()
    print('-'*13)
    print('|' + ' '*3 + '|' + ' '*3 + '|' + ' '*3 + '|')
    print('|' + ' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9] + ' ' + '|')
    print('|' + ' '*3 + '|' + ' '*3 + '|' + ' '*3 + '|')
    print('-'*13)
    print('|' + ' '*3 + '|' + ' '*3 + '|' + ' '*3 + '|')
    print('|' + ' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6] + ' ' + '|')
    print('|' + ' '*3 + '|' + ' '*3 + '|' + ' '*3 + '|')
    print('-'*13)
    print('|' + ' '*3 + '|' + ' '*3 + '|' + ' '*3 + '|')
    print('|' + ' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3] + ' ' + '|')
    print('|' + ' '*3 + '|' + ' '*3 + '|' + ' '*3 + '|')
    print('-'*13)

def player_input():
    
    marker = ''
    first_marker = ''
    second_marker = ''
    
    while(marker!='X' and marker!='O'):
        marker=input(f"{players[first_player]['Player']} Pick a marker, X or O into this box: ").upper()
    
    first_marker = marker

    if first_marker == 'X':
        second_marker = 'O'
    else:
        second_marker = 'X'
        
    return (first_marker, second_marker)

def place_marker(board, marker, position):
    board[position] = marker
    return board

def win_check(board, mark):
    if(board[1]==board[2]==board[3]==mark):
        return True
    elif(board[4]==board[5]==board[6]==mark):
        return True
    elif(board[7]==board[8]==board[9]==mark):
        return True
    elif(board[1]==board[4]==board[7]==mark):
        return True
    elif(board[2]==board[5]==board[8]==mark):
        return True
    elif(board[3]==board[6]==board[9]==mark):
        return True
    elif(board[1]==board[5]==board[9]==mark):
        return True
    elif(board[3]==board[5]==board[7]==mark):
        return True
    else:
        return False

def choose_first():
    return randint(1,2)

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    isFull = ' ' not in board
    return isFull

def player_choice(board):
    invalid = False
    position = 0
    while(not invalid):
        position=(input('Place your next position: '))
        if position.isdigit() and int(position) in range(1,10):
            invalid = space_check(board, int(position))
        else:
            continue
    return int(position)

def replay():
    answer = ''
    while(answer!='Yes' and answer!='No'):
        answer=(input('Do you want yo play again? Yes / No: '))
    if(answer=='Yes'):
        return True
    else:
        return False
        

# print('Welcome to Tic Tac Toe!')

play = True

while play:
    # Set the game up here
    #Clean board
    #board = ['#']+([' ']*9)
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    #Variable initialization
    #winner = False
    #full = False
    
    
    first_player = 0
    first_marker = ''
    second_player = 0
    second_marker = ''
    
    position = 0
    
    #Players information
    players = {1: {'Marker': '', 'Player': 'Player 1'}, 2: {'Marker': '', 'Player': 'Player 2'}}
    
    #Turns
    turns = {1: '', 2: ''}
    
    #Turns selection
    first_player = choose_first()
    
    if(first_player==1):
        second_player=2
    else:
        second_player=1
    
    #Turns assembly
    turns[1] = players[first_player]
    turns[2] = players[second_player]
    
    first_marker, second_marker = player_input()
    
    #Marker assignment
    turns[1]['Marker'] = first_marker
    turns[2]['Marker'] = second_marker
    
    while True:
        
        display_board(board)
        
        #Player 1 Turn
        position = player_choice(board)
        board = place_marker(board, first_marker, position)
        display_board(board)
        
        if win_check(board, first_marker):
            print(f'{first_marker} Won the game')
            break
        
        if full_board_check(board):
            print('There is a tie, nobody Won the game')
            break
        
        # Player2's turn.
        position = player_choice(board)
        board = place_marker(board, second_marker, position)
        display_board(board)
        
        if win_check(board, second_marker):
            print(f'{second_marker} Won the game')
            break
        
        if full_board_check(board):
            print('There is a tie, nobody Won the game')
            break
    
    play = replay()