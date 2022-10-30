from re import X

board = {'top_L':' ', 'top_M':' ', 'top_R':' ',
        'mid_L':' ', 'mid_M':' ', 'mid_R':' ',
        'bot_L':' ', 'bot_M':' ', 'bot_R':' '
        }

def display_board():
    print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
    print("-+-+-")
    print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'])
    print("-+-+-")
    print(board['bot_L'] + '|' + board['bot_M'] + '|' + board['bot_R'])

def player1():
    location = input("Player 1 enter location for x ")
    board[location] = 'x'
    display_board()

def player2():
    location = input("Player 2 enter location for o ")
    board[location] = 'o'
    display_board()

#Display empty board
display_board()

turn = 'X'

for loop in range(0,9):
    if turn == 'X':
        player1()
        turn = 'Y'
    else:
        player2()
        turn = 'X'

