import sys

def babybites(lines):
    nums = [x for x in lines[1].split(" ")]

    expectedNum = 1
    for num in nums:
        if num != "mumble":
            if int(num) != expectedNum:
                return "something is fishy"
        expectedNum += 1
    return "makes sense"


def main():
    lines = [line.strip() for line in sys.stdin]
    print(babybites(lines))
main()
