import sys

def zigzag2(lines):
    numbers = sorted([int(num) for num in lines[1:]])
    left_index = 0
    right_index = len(numbers) - 1


def main():
    lines = [line.strip() for line in sys.stdin]
    print(zigzag2(lines))
main()
