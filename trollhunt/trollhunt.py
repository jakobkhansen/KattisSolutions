import sys

def trollhunt(lines):
    numBridges = int(lines[0].split(" ")[0]) - 1
    numKnights = int(lines[0].split(" ")[1])
    numGroupSize = int(lines[0].split(" ")[2])

    numGroups = numKnights // numGroupSize

    if numBridges % numGroups == 0:
        numDays = int(numBridges / numGroups)

    else:
        numDays = int(numBridges // numGroups + 1)

    return numDays

def main():
    lines = [line.strip() for line in sys.stdin]
    print(trollhunt(lines))
main()
