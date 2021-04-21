import sys
import math

def egypt(lines):
    for line in lines[:-1]:
        a,b,c = sorted([int(x) for x in line.split(" ")])
        hyp = math.sqrt(a**2 + b**2)
        print("right" if hyp == c else "wrong")


def main():
    lines = [line.strip() for line in sys.stdin]
    (egypt(lines))
main()
