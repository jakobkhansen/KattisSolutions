import sys

def nineknights(lines):
    moves = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (2, 1),
        (2, -1),
        (1, 2),
        (1, -2)
    ]
    board = [list(x) for x in lines]
    num_knights = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "k":
                num_knights += 1
                for dx,dy in moves:
                    x,y = i+dx,j+dy 
                    if inbounds(x,y,board) and board[x][y] == "k":
                        return "invalid"
    return "valid" if num_knights == 9 else "invalid"

def inbounds(x,y,board):
    return x >= 0 and x < len(board) and y >= 0 and y < len(board)

def main():
    lines = [line.strip() for line in sys.stdin]
    print(nineknights(lines))
main()
