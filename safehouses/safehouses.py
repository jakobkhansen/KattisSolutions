import sys
import math

def safehouses(lines):
    spies = []
    safehouses = []

    size = int(lines[0])

    grid = [list(x) for x in lines[1:]]


    for i in range(size):
        for j in range(size):
            if grid[i][j] == "H":
                safehouses.append((i,j))
            elif grid[i][j] == "S":
                spies.append((i,j))


    maxMinDistance = 0

    for spy in spies:
        minDistanceForSpy = sys.maxsize
        for safehouse in safehouses:
            distance = abs(spy[0] - safehouse[0]) + abs(spy[1] - safehouse[1])
            if distance < minDistanceForSpy:
                minDistanceForSpy = distance
        if minDistanceForSpy > maxMinDistance:
            maxMinDistance = minDistanceForSpy

    return maxMinDistance




def main():
    lines = [line.strip() for line in sys.stdin]
    print(safehouses(lines))
main()
