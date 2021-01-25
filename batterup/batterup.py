import sys

def batterup(lines):
    nums = [int(x) for x in lines[1].split(" ")]

    nums = list(filter(lambda x: x != -1, nums))

    return sum(nums)/len(nums)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(batterup(lines))
main()
