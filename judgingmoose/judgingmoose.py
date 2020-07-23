import sys

def judgingmoose(lines):
    nums = [int(x) for x in lines[0].split()]
    left = nums[0]
    right = nums[1]

    if (left == right):
        if (left == 0):
            return "Not a moose"
        return "Even {}".format(left*2)

    return "Odd {}".format(max(left, right)*2)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(judgingmoose(lines))
main()
