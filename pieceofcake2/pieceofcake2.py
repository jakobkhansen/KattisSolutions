import sys

def pieceofcake2(lines):
    nums = [int(x) for x in lines[0].split(" ")]
    n = nums[0]
    h = nums[1]
    v = nums[2]

    return max([h*v, (n-v)*h, (n-h)*v, (n-v)*(n-h)])*4


def main():
    lines = [line.strip() for line in sys.stdin]
    print(pieceofcake2(lines))
main()
