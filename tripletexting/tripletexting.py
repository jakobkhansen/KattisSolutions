import sys

def tripletexting(lines):
    line = lines[0]
    length = len(line)//3

    words = [line[i:length+i] for i in range(0, len(line), length)]

    uniques = set()
    for word in words:
        if word in uniques:
            return word
        uniques.add(word)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(tripletexting(lines))
main()
