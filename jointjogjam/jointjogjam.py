import sys

def jointjogjam(lines):
    nums = [int(x) for x in lines[0].split()]
    x1_start, y1_start, x2_start, y2_start, x1_end, y1_end, x2_end, y2_end = nums

    dist1 = ((((x2_start - x1_start )**2) + ((y2_start-y1_start)**2) )**0.5)
    dist2 = ((((x2_end - x1_end )**2) + ((y2_end-y1_end)**2) )**0.5)

    return max(dist1, dist2)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(jointjogjam(lines))
main()
