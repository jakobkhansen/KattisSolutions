import sys

def pet(lines):
    sums = []
    for i in lines:
        sums.append(sum([int(x) for x in i.split(" ")]))
    largest, index = max(sums), sums.index(max(sums)) + 1
    return "{} {}".format(index, largest)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(pet(lines))
main()
