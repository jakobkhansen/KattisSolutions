import sys

class Platform:
    def __init__(self, left, right, alt):
        self.left = left
        self.right = right
        self.alt = alt

def platforme(lines):
    platforms = []

    for platform in lines[1:]:
        nums = [int(x) for x in platform.split()]
        alt = nums[0]
        left = nums[1]
        right = nums[2]
        platforms.append(Platform(left, right, alt))

    totalHeight = 0
    for platform in platforms:
        leftFloor = 0
        rightFloor = 0

        for floor in platforms:
            if floor.alt < platform.alt:
                if floor.left <= platform.left < floor.right and floor.alt > leftFloor:
                    leftFloor = floor.alt

                if floor.left < platform.right <= floor.right and floor.alt > rightFloor:
                    rightFloor = floor.alt

        totalHeight += platform.alt - leftFloor
        totalHeight += platform.alt - rightFloor


    return totalHeight


def main():
    lines = [line.strip() for line in sys.stdin]
    print(platforme(lines))
main()
