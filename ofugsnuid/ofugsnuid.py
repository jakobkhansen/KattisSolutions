import sys

def ofugsnuid(lines):
    nums = [print(x) for x in reversed(lines[1:])]

def main():
    lines = [line.strip() for line in sys.stdin]
    ofugsnuid(lines)
main()
