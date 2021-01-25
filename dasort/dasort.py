import sys

def dasort(lines):
    p = int(lines[0].split()[0])
    retString = ""
    index = 1
    caseNum = 1
    for i in range(p):
        numElems = int(lines[index].split(" ")[1])
        index += 1
        dvds = []
        while len(dvds) < numElems:
            dvds = dvds + [int(x) for x in lines[index].split(" ")]
            index += 1
        retString += str(caseNum) + " " + str(countMoves(dvds)) + "\n"
        caseNum += 1

    return retString.strip()

def countMoves(dvds):
    numMoves = len(dvds)
    sortedDvds = sorted(dvds)
    expectedItem = 0

    for i in range(len(dvds)):
        if dvds[i] == sortedDvds[expectedItem]:
            expectedItem += 1
            numMoves -= 1
    return numMoves



def main():
    lines = [line.strip() for line in sys.stdin]
    print(dasort(lines))
main()
