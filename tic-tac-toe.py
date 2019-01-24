import random
from time import sleep

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def win(board):
    if board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X':
        return True
    if board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X':
        return True
    if board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X':
        return True
    if board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L'] == 'X':
        return True
    if board['top-M'] == 'X' and board['mid-M'] == 'X' and board['low-M'] == 'X':
        return True
    if board['top-R'] == 'X' and board['mid-R'] == 'X' and board['low-R'] == 'X':
        return True
    if board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X':
        return True
    if board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L'] == 'X':
        return True
    if board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R'] == 'O':
        return True
    if board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R'] == 'O':
        return True
    if board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O':
        return True
    if board['top-L'] == 'O' and board['mid-L'] == 'O' and board['low-L'] == 'O':
        return True
    if board['top-M'] == 'O' and board['mid-M'] == 'O' and board['low-M'] == 'O':
        return True
    if board['top-R'] == 'O' and board['mid-R'] == 'O' and board['low-R'] == 'O':
        return True
    if board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O':
        return True
    if board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-L'] == 'O':
        return True


def play_game():
    print('Welcome to Tic Tac Toe!')
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '
                }
    orders = list(theBoard.keys())
    random.shuffle(orders)
    turn = 'X'
    winner = -1
    for i in range(len(orders)):
        printBoard(theBoard)
        print('Turn for ' + turn + '.')
        sleep(2)
        theBoard[orders[i]] = turn

        if win(theBoard):
            winner = turn
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    printBoard(theBoard)

    if winner == -1:
        print("There's a tie!")
    else:
        print("Winner is: " + winner)


play_game()