import sys

def watchdog(lines):
    cases = int(lines[0])
    index = 1
    for _ in range(cases):
        s,h = [int(x) for x in lines[index].split()]
        c_x,c_y = 0,0
        for i in range(h):
            x,y = [int(x) for x in lines[index+i+1].split()]
            c_x += x
            c_y += y
        c_x /= h
        c_y /= h
        print(c_x, c_y)
        index += h +1

def get_centroid(hatches):
    pass


def main():
    lines = [line.strip() for line in sys.stdin]
    print(watchdog(lines))
main()
