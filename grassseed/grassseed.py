import sys

def grassseed(lines):
    price = float(lines[0].split(" ")[0])
    lines = lines[2:]

    ret = 0
    for i in lines:
        nums = i.split(" ")
        num1 = float(nums[0])
        num2 = float(nums[1])

        ret += num1*num2*price
    return ret


def main():
    lines = [line.strip() for line in sys.stdin]
    print(grassseed(lines))
main()
