import sys

def shatteredcake(lines):
    width = int(lines[0])
    area = 0
    for piece in lines[2:]:
        x,y = [int(x) for x in piece.split()]
        area += x*y
    return int(area / width)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(shatteredcake(lines))
main()
