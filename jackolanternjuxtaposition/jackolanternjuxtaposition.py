import sys

def jackolanternjuxtaposition(lines):
    nums = [int(x) for x in lines[0].split(" ")]
    return nums[0] * nums[1] * nums[2]


def main():
    lines = [line.strip() for line in sys.stdin]
    print(jackolanternjuxtaposition(lines))
main()
