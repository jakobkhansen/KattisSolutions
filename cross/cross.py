import sys
import math

def cross(lines):
    board = [[x for x in y] for y in lines]

    memory = build_memory(board)

    if not verify_board(memory):
        print("ERROR")
        return

    continue_flag = True

    boxes = get_boxes()
    while continue_flag:
        continue_flag = False
        for number in range(1, 10):
            # print("Trying number {}".format(number))
            number = str(number)
            number_flag = True
            for box in boxes:
                box_copy = box.copy()
                if any([x in box_copy for x in memory.get(number, [])]):
                    continue

                box_copy = [x for x in box_copy if board[x[0]][x[1]] == '.']
                for existing_number in memory.get(number, []):
                    box_copy = [x for x in box_copy if not in_same_row(existing_number, x) and not in_same_column(existing_number, x)]


                # print(box_copy)
                if len(box_copy) == 1:
                    x,y = box_copy[0]
                    board[x][y] = number

                    pos_list = memory.get(number, [])
                    pos_list.append((x,y))
                    memory[number] = pos_list

                    number_flag = False
                    continue_flag = True

                    break
                elif len(box_copy) == 0:
                    print("ERROR")
                    return
            if not number_flag:
                break
    print_board(board)


                        


def get_boxes():
    # Too tired for this shit
    boxes = [
        [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)],
        [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)],
        [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)],

        [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)],
        [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)],
        [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)],

        [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)],
        [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)],
        [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)],
    ]

    return boxes


def build_memory(board):
    numbers = {}
    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if cell != '.':
                number_list = numbers.get(cell, [])
                number_list.append((i,j))
                numbers[cell] = number_list
    return numbers

def verify_board(memory):
    numbers = memory.keys()
    for number in numbers:
        for i in range(len(memory[number])):
            cell1 = memory[number][i]
            for j in range(i+1, len(memory[number])):
                cell2 = memory[number][j]
                if in_same_row(cell1, cell2) or in_same_column(cell1, cell2) or in_same_box(cell1, cell2):
                    return False
    return True


def in_same_row(cell1, cell2):
    return cell1[0] == cell2[0]

def in_same_column(cell1, cell2):
    return cell1[1] == cell2[1]

def in_same_box(cell1, cell2):
    cell1_row_box = math.floor(cell1[0] / 3)
    cell1_column_box = math.floor(cell1[1] / 3)

    cell2_row_box = math.floor(cell2[0] / 3)
    cell2_column_box = math.floor(cell2[1] / 3)

    return (cell1_row_box, cell1_column_box) == (cell2_row_box, cell2_column_box)



def print_board(board):
    out = []
    for line in board:
        out.append("".join(line))
    print("\n".join(out))

def main():
    lines = [line.strip() for line in sys.stdin]
    cross(lines)
main()
