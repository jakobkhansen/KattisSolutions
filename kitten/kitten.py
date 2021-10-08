import sys

def kitten(lines):
    kitty = int(lines[0])
    parents = {}

    for line in lines[1:]:
        split = line.split()
        parent = int(split[0])
        for child in split[1:]:
            parents[int(child)] = parent

    current = kitty
    while current is not None:
        print(current, end=" ")
        current = parents.get(current, None)




def main():
    lines = [line.strip() for line in sys.stdin]
    (kitten(lines))
main()
