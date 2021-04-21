import sys
from fractions import Fraction

def prsteni(lines):
    nums = [int(x) for x in lines[1].split(" ")]
    base = nums[0]

    for num in nums[1:]:
        res = str(Fraction(base/num))
        if not "/" in res:
            res += "/1"
        print(res)


def main():
    lines = [line.strip() for line in sys.stdin]
    (prsteni(lines))
main()
