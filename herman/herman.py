import sys
import math

def herman(lines):
    retString = ""
    radius = int(lines[0].split(" ")[0])
    retString += str(eucledian(radius)) + "\n"
    retString += str(taxicab(radius))

    return retString


def eucledian(radius):
    return math.pi*(radius**2)

def taxicab(radius):
    return 2*(radius**2)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(herman(lines))
main()
