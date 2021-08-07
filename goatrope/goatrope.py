import sys
import math

def goatrope(lines):
    x,y,x1,y1,x2,y2 = [int(x) for x in lines[0].split()]
    x3,y3 = x1,y2
    x4,y4 = x2,y1

    min_x = min(x1,x2)
    min_y = min(y1,y2)
    max_x = max(x1,x2)
    max_y = max(y1,y2)

    dx = max(min_x - x, 0, x - max_x);
    dy = max(min_y - y, 0, y - max_y);
    return math.sqrt(dx*dx + dy*dy);


def main():
    lines = [line.strip() for line in sys.stdin]
    print(goatrope(lines))
main()
