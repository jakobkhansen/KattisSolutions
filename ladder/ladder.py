import sys 
import math


def ladder(lines):
    opposite = int(lines[0].split(" ")[0])
    angle = math.radians(int(lines[0].split(" ")[1]))
    hypotenus = math.ceil(opposite / math.sin(angle))

    return hypotenus






def main():
    lines = [line.strip() for line in sys.stdin]
    print(ladder(lines))
main()
