import sys

def reversebinary(lines):
    num = int(lines[0])
    binString = bin(num)[2:]
    binStringRev = binString[::-1]
    return int (binStringRev, 2)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(reversebinary(lines))
main()
