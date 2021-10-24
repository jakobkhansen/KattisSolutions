import sys

def twosum(lines):
    return sum([int(x) for x in lines[1].split()])

def main():
    lines = [line.strip() for line in sys.stdin]
    print(twosum(lines))
main()
