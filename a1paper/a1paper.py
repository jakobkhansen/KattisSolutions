import sys

def a1paper(lines):
    numTypes = int(lines[0].split(" ")[0])
    numPapers = [int(x) for x in lines[1].split(" ")]
    sizes = getSizes(numTypes)
    return str(tapeLengthReallyFast(numPapers, sizes))


def getSizes(numTypes):
    size = [0]*numTypes
    vertical = 2**(-3/4)
    horizontal = 2**(-5/4) 

    for i in range(0, numTypes, 2):
        size[i] = vertical
        vertical /= 2

    for i in range(1, numTypes, 2):
        size[i] = horizontal
        horizontal /= 2

    return size

def tapeLength(numPapers, sizes):
    total = sizes[0]
    changed = True
    while (numPapers[0] < 2 and changed):
        changed = False
        for i in range(1, len(numPapers)):
            if numPapers[i] >= 2:
                numPapers[i-1] += 1
                numPapers[i] -= 2
                total += sizes[i]
                changed = True

    if numPapers[0] < 2:
        return "impossible"

    return total

def tapeLengthFast(numPapers, sizes):
    total = sizes[0]
    i = 1
    while (0 < i < len(numPapers)):
        if numPapers[i] >= 2:
            numPapers[i-1] += 1
            numPapers[i] -= 2
            total += sizes[i]

        if numPapers[i-1] >= 2:
            i -= 1
        elif numPapers[i] < 2:
            i += 1


    if numPapers[0] < 2:
        return "impossible"

    return total

def tapeLengthReallyFast(numPapers, sizes):
    total = 0
    needed = 2
    for i in range(len(numPapers)):

        print(total)
        print(numPapers[i])

        if numPapers[i] >= needed:
            total += sizes[i]
            needed = 0
            break

        else:
            total += sizes[i] * (numPapers[i] / needed)
            needed -= numPapers[i]

        needed*=2
        print("")

    if needed != 0:
        return "impossible"
    return total


def main():
    lines = [line.strip() for line in sys.stdin]
    print(a1paper(lines))
main()
