import sys
import math

def soylent(lines):
    for line in lines[1:]:
        cals = int(line)
        num_bottles = math.ceil(cals / 400)

        print(num_bottles)

def main():
    lines = [line.strip() for line in sys.stdin]
    soylent(lines)
main()
