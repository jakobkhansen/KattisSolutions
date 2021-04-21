import sys

def jumbojavelin(lines):
    return sum([int(x)-1 for x in lines[1:]]) + 1


def main():
    lines = [line.strip() for line in sys.stdin]
    print(jumbojavelin(lines))
main()
