import sys

def queens(lines):

    # Check all lines
    lines_x = [int(x.split()[0]) for x in lines[1:]]
    lines_y = [int(x.split()[1]) for x in lines[1:]]

    if len(lines_x) != len(list(set(lines_x))) or len(lines_y) != len(list(set(lines_y))):
        return "INCORRECT"

    n = int(lines[0].split()[0])
    queens = [list(map(int, x.split())) for x in lines[1:]]

    board =  [ [ "." for i in range(n) ] for j in range(n) ]

    for x,y in queens:
        board[x][y] = "Q"


    for x,y in queens:
        if queenExistsOnDiagonal(board, x, y):
            return "INCORRECT"

    return "CORRECT"

def printBoard(board):
    print("BOARD:")

    for row in board:
        print(row)

def queenExistsOnDiagonal(board, x, y):
    i = x
    j = y
    while i > 0 and j > 0:
        i -= 1
        j -= 1

        if board[i][j] == "Q":
            return True

    i = x
    j = y
    while i > 0 and j < len(board)-1:
        i -= 1
        j += 1

        if board[i][j] == "Q":
            return True
    i = x
    j = y
    while i < len(board)-1 and j < len(board)-1:
        i += 1
        j += 1

        if board[i][j] == "Q":
            return True

    i = x
    j = y
    while i < len(board)-1 and j > 0:
        i += 1
        j -= 1

        if board[i][j] == "Q":
            return True

    return False

def main():
    lines = [line.strip() for line in sys.stdin]
    print(queens(lines))
main()
