import sys

def arithmetic(lines):
    return hex(int(lines[0], 8))[2:].upper()


def main():
    lines = [line.strip() for line in sys.stdin]
    print(arithmetic(lines))
main()
