import sys
import math

def pizza2(lines):
    R,C = [int(x) for x in lines[0].split(" ")]

    P = R - C

    return ((math.pi*(P**2)) / (math.pi*(R**2))) * 100


def main():
    lines = [line.strip() for line in sys.stdin]
    print(pizza2(lines))
main()
