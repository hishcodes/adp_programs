from re import X
import sys

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

def is_won():
    if ((board['top_L'] == board['top_M'] == board['top_R'] == turn) or
        (board['mid_L'] == board['mid_M'] == board['mid_R'] == turn) or
        (board['bot_L'] == board['bot_M'] == board['bot_R'] == turn) or
        (board['top_L'] == board['mid_L'] == board['bot_L'] == turn) or
        (board['top_M'] == board['mid_M'] == board['bot_M'] == turn) or
        (board['top_R'] == board['mid_R'] == board['bot_R'] == turn) or
        (board['top_L'] == board['mid_M'] == board['bot_R'] == turn) or
        (board['top_R'] == board['mid_M'] == board['bot_L'] == turn)):
        return True
    else:
        return False


def player1():
    location = input("Player 1 enter location for x ")
    board[location] = 'x'
    display_board()
    if is_won():
        print("Player 1 won")
        sys.exit()

def player2():
    location = input("Player 2 enter location for o ")
    board[location] = 'o'
    display_board()
    if is_won():
        print("Player 2 won")
        sys.exit()

#Display empty board
display_board()

turn = 'x'

for loop in range(0,9):
    if turn == 'x':
        player1()
        turn = 'o'
    else:
        player2()
        turn = 'x'
    if loop == 8:
        print("Match draw")
