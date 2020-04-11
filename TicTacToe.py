""" This is a tic-tac-toe game that can be played in 2 players """ 
import random

board = {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'
    }
def show_board():
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

def twoplayers():

    sym=input("Choose a symbol: [X/0] ").upper()
    while True:
        show_board()
        print("Turn for:", sym)
        pos = input("Choose a space: ")

        for i in board:
            if i==pos:
                if board[i]!='X'and board[i]!='0':
                    board[i]=sym
                else:
                    pos=input("Taken! Choose again: ")

        if sym=='X':
            sym='0'
        else:
            sym='X'

        if board['1'] == board['2'] == board['3'] or\
            board['4'] == board['5'] == board['6'] or\
            board['7'] == board['8'] == board['9'] or\
            board['1'] == board['4'] == board['7'] or\
            board['2'] == board['5'] == board['8'] or\
            board['3'] == board['6'] == board['9'] or \
            board['1'] == board['5'] == board['9'] or \
            board['3'] == board['5'] == board['7']:

            if sym=='X':
                show_board()
                print("Winner is: 0")
                break
            elif sym=='0':
                show_board()
                print("Winner is: X")
                break
        if board['1']=='1' or board['2']=='2' or board['3']=='3'\
            or board['4']=='4' or board['5']=='5' or board['6']=='6'\
            or board['7']=='7' or board['8']=='8' or board['9']=='9':
            continue
        else:
            print("Draw")
            break
    opt = input("One more game? [Y/N] ").upper()
    if opt == 'Y':
        onemore()
    else:
        print("Bye-Bye")

def onemore():

    board = {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'
        }
    twoplayers()


