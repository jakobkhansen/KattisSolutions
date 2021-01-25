import sys

def aaah(lines):
    res = len(lines[0]) >= len(lines[1])

    return "go" if res else "no"


def main():
    lines = [line.strip() for line in sys.stdin]
    print(aaah(lines))
main()
