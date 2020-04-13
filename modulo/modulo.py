import sys

def modulo(lines):
    nums = [int(x.split(" ")[0]) for x in lines]
    uniques = {}
    for num in nums:
        uniques[num % 42] = 1

    return len(uniques.keys())


def main():
    lines = [line.strip() for line in sys.stdin]
    print(modulo(lines))
main()
