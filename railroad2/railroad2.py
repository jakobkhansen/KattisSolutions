import sys

def railroad2(lines):
    x,y = [int(x) for x in lines[0].split(" ")]

    return "possible" if ((x*4)+(y*3)) % 2 == 0 else "impossible"


def main():
    lines = [line.strip() for line in sys.stdin]
    print(railroad2(lines))
main()
