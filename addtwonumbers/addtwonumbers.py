import sys

def addtwonumbers(lines):
    nums = [int(x) for x in lines[0].split()]
    return sum(nums)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(addtwonumbers(lines))
main()
