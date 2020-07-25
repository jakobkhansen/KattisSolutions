import sys

def shopaholic(lines):
    items = [int(x) for x in lines[1].split()]
    items.sort(reverse=True)

    return sum(items[2::3])


def main():
    lines = [line.strip() for line in sys.stdin]
    print(shopaholic(lines))
main()
