import sys
from enum import Enum

def turtlemaster(lines):
    board = []
    moves = lines[-1]
    lines = lines[:-1]

    for line in lines:
        line_list = []
        for char in line:
            line_list.append(char)
        board.append(line_list)

    position, direction = (len(board) - 1, 0), DirectionEnum(1)
    # print(board)

    position = move(board, position, direction)
    print(board)

def turn(direction, current):
    if direction == "R":
        if current.value == 4:
            return DirectionEnum(1)
        return DirectionEnum(current.value + 1)
    elif direction == "L":
        if current.value == 1:
            return DirectionEnum(4)
        return DirectionEnum(current.value - 1)



def move(board, position, direction):
    print(position[0])

    

    new_position = get_next_coordinate(position, direction)
    new_symbol = board[new_position[0]][new_position[1]]
    if any(n < 0 for n in new_position):
        return "Bug!"

    if new_symbol == "I" or new_symbol == "C":
        return "Bug!"

    board[position[0]][position[1]] = "."
    board[new_position[0]][new_position[1]] = "T"

    return new_position

def shoot(board, position, direction):
    target_position = get_next_coordinate(position, direction)
    target_symbol = 


class DirectionEnum(Enum):
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    UP = 4

def get_next_coordinate(position, direction):

    coordinateSwitcher = {
        DirectionEnum.RIGHT: (position[0], position[1] + 1),
        DirectionEnum.DOWN: (position[0] + 1, position[1]),
        DirectionEnum.LEFT: (position[0], position[1] - 1),
        DirectionEnum.UP: (position[0] - 1, position[1])
    }

    return coordinateSwitcher.get(direction)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(turtlemaster(lines))
main()
