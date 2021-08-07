import sys

def different(lines):
    for line in lines:
        x,y = [int(x) for x in line.split()]
        print(abs(x - y))


def main():
    lines = [line.strip() for line in sys.stdin]
    (different(lines))
main()
