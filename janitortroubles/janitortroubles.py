import sys
import math

def janitortroubles(lines):
    a,b,c,d = [int(x) for x in lines[0].split(" ")]

    print(a,b,c,d)

    s = (a+b+c+d)/2

    base = (s-a)*(s-b)*(s-c)*(s*d) - (a*b*c*d) * math.cos((b+d)/2) ** 2

    return math.sqrt(base)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(janitortroubles(lines))
main()
