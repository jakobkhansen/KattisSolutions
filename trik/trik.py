import sys

def trik(lines):
    moves = lines[0]
    cups = [1, 0, 0]

    for char in moves:
        if char == 'A':
            temp = cups[0]
            cups[0] = cups[1]
            cups[1] = temp

        elif char == 'B':
            temp = cups[1]
            cups[1] = cups[2]
            cups[2] = temp

        else:
            temp = cups[0]
            cups[0] = cups[2]
            cups[2] = temp

    for i in range(len(cups)):
        if cups[i] == 1:
            return i + 1



def main():
    lines = [line.strip() for line in sys.stdin]
    print(trik(lines))
main()
