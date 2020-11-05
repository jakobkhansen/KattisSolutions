import sys

def dvds(lines):
    k = int(lines[0].split()[0])
    lines = lines[1:]
    retString = ""
    for i in range(k):
        n = int(lines[0].split()[0])
        dvds = [int(x) for x in lines[1].split()]
        lines = lines[2:]
        retString += str(countMoves(dvds)) + "\n"

    return retString.strip()

def countMoves(dvds):
    numMoves = len(dvds)
    expectedItem = 1

    for i in range(len(dvds)):
        if dvds[i] == expectedItem:
            expectedItem += 1
            numMoves -= 1
    return numMoves


def main():
    lines = [line.strip() for line in sys.stdin]
    print(dvds(lines))
main()
