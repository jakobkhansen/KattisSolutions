import sys

def knotknowledge(lines):
    first = sum([int(x) for x in lines[1].split()])
    second = sum([int(x) for x in lines[2].split()])

    return first - second


def main():
    lines = [line.strip() for line in sys.stdin]
    print(knotknowledge(lines))
main()
