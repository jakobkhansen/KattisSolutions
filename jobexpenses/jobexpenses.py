import sys
import math

def jobexpenses(lines):
    if len(lines[1]) == 0:
        return 0

    nums = [int(x) for x in lines[1].split(" ") if int(x) < 0]


    return abs(sum(nums))

def main():
    lines = [line.strip() for line in sys.stdin]
    print(jobexpenses(lines))
main()
