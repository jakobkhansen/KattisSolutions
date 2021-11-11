import sys

def shortlex(lines):
    t,*nums = [int(x) for x in lines]
    for num in nums:
        chars = []


def main():
    lines = [line.strip() for line in sys.stdin]
    print(shortlex(lines))
main()
