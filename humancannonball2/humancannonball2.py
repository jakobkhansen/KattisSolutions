import sys
from math import cos,sin,radians

def humancannonball2(lines):
    for case in lines[1:]:
        v_0,ang,dist,h_1,h_2 = [float(x) for x in case.split()]
        t = (dist)/(v_0*cos(radians(ang)))
        y = v_0*t*sin(radians(ang)) - (1/2)*(9.81)*t**2
        out = "Safe" if (h_1+1) < y < (h_2-1) else "Not Safe"
        print(out)


def main():
    lines = [line.strip() for line in sys.stdin]
    (humancannonball2(lines))
main()
