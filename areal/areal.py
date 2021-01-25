import sys
import math

def areal(lines):
    return math.sqrt(int(lines[0]))*4


def main():
    lines = [line.strip() for line in sys.stdin]
    print(areal(lines))
main()
