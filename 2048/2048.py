import sys

def tfe(lines):
    matrix = [[int(x) for x in y.split(" ")] for y in lines[:-1]]
    direction = int(lines[-1]) 

    if direction == 0:
        left(matrix)
    elif direction == 1:
        transpose(matrix)
        left(matrix)
        transpose(matrix)
    elif direction == 2:
        right(matrix)
    elif direction == 3:
        transpose(matrix)
        right(matrix)
        transpose(matrix)

    return print_matrix(matrix).strip()

def left(board):
    for row in board:
        for i in range(len(row)-1):
            while row[i] == 0 and any(row[i:]):
                # print("yes")
                row.pop(i)
                row.append(0)
            j = i+1
            while j < len(row)-1 and row[j] == 0:
                j += 1
            if row[i] == row[j]:
                row[i] *= 2
                row.pop(j)
                row.append(0)

def right(board):
    for row in board:
        for i in range(len(row)-1, 0, -1):
            # print(i)
            # print(print_matrix(board))
            # print(row[:i])
            while row[i] == 0 and any(row[:i]):
                row.pop(i)
                row.insert(0, 0)
            j = i-1
            while j >= 1 and row[j] == 0:
                j -= 1
            if row[i] == row[j]:
                row[i] *= 2
                row.pop(j)
                row.insert(0, 0)

def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

def print_matrix(matrix):
    ret = ""
    for row in matrix:
        for number in row:
            ret += str(number) + " "
        ret.strip()
        ret += "\n"
    return ret


        

def main():
    lines = [line.strip() for line in sys.stdin]
    print(tfe(lines))
main()
