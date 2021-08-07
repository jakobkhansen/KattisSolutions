import sys

def sorttwonumbers(lines):
    nums = [int(x) for x in lines[0].split()]
    return " ".join([str(x) for x in sorted(nums)])


def main():
    lines = [line.strip() for line in sys.stdin]
    print(sorttwonumbers(lines))
main()
