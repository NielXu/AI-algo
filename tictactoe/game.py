"""
Classic tic tac toe game, does not handle any kinds
of errors.
"""
from copy import deepcopy
import minimax


ENABLE_AI = True


def init_board():
    "Initializing a board and return it as a nested list"
    return [["-" for x in range(3)] for x in range(3)]


def make_move(board, x, y, p):
    "Make move, set O if it is player or X if it is computer at (x,y)"
    board[x][y] = "O" if p == True else "X"


def check(board):
    """Check if there is any winner on the board, return 1 if computer win,
    0 if player win, None if no winner
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '-':
            return 1 if board[i][0] == "X" else 0
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '-':
            return 1 if board[0][i] == "X" else 0
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
            return 1 if board[0][0] == "X" else 0
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
            return 1 if board[0][2] == "X" else 0


def is_full(board):
    "Check if board is full"
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True


def is_placed(board, x, y):
    "Check if (x,y) had been placed or not"
    return board[x][y] != '-'


def cp_board(board):
    "Make a copy of the board without changing the original one"
    return deepcopy(board)

def show(board):
    "Print board nicely"
    for i in range(3):
        row = ''
        for j in range(3):
            row += board[i][j]
            if j != 2:
                row += ' | '
        print(row)
        if i != 2:
            print("----------")
    print("**************************")
    print()


def undo(board, x, y):
    "Undo move at (x,y)"
    board[x][y] = '-' 


def game():
    b = init_board()
    p = True
    while True:
        show(b)
        if p:
            x,y = input("Eneter your move(Player):").split(",")
            make_move(b, int(x), int(y), p)
            p = False
        else:
            if ENABLE_AI:
                x,y = minimax.gen(b)
            else:
                x,y = input("Eneter your move(Computer)").split(",")
            make_move(b, int(x), int(y), p)
            p = True
        result = check(b)
        if result == 0:
            print("Congraz, u win!")
            break
        elif result == 1:
            print("Sorry, computer win")
            break
        else:
            if is_full(b):
                print("Draw")
                break
    show(b)


def start():
    while True:
        game()
        again = input("Do you wanna try again?(y/n)")
        if again == 'n':
            break
        print()

if __name__ == "__main__":
    start()
