import sys

def laptopsticker(lines):
    w1, h1, w2, h2 = [int(x) for x in lines[0].split()]
    diff1, diff2 = (w1 - w2), (h1 - h2)

    return 1 if diff1 >= 2 and diff2 >= 2 else 0



def main():
    lines = [line.strip() for line in sys.stdin]
    print(laptopsticker(lines))
main()
