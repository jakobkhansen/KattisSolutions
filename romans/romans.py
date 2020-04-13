import sys

def romans(lines):
    num = float(lines[0].split(" ")[0])

    return round(num * 1000 * (5280/4854))


def main():
    lines = [line.strip() for line in sys.stdin]
    print(romans(lines))
main()
