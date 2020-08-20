import sys

def sodaslurper(lines):
    nums = [int(x) for x in lines[0].split(" ")]
    start = nums[0]
    found = nums[1]
    cost = nums[2]

    current = start + found

    bought = 0
    while (current >= cost):
        bought += 1
        current -= cost - 1

    return bought


def main():
    lines = [line.strip() for line in sys.stdin]
    print(sodaslurper(lines))
main()
