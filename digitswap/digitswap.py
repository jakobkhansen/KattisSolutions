import sys

def digitswap(lines):
    return "".join(reversed(lines[0]))


def main():
    lines = [line.strip() for line in sys.stdin]
    print(digitswap(lines))
main()
