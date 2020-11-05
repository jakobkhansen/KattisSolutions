import sys

def licensetolaunch(lines):
    nums = [int(x) for x in lines[1].split(" ")]

    return nums.index(min(nums))


def main():
    lines = [line.strip() for line in sys.stdin]
    print(licensetolaunch(lines))
main()
