import sys

def ants():
    numCases = int(sys.stdin.readline())

    for case in range(numCases):
        length, numAnts = [int(x) for x in sys.stdin.readline().split(" ")]
        readAnts = 0

        closestToMedian = 0
        farthestFromMedian = 0

        while readAnts != numAnts:
            newAnts = [int(x) for x in sys.stdin.readline().split(" ")]
            for ant in newAnts:
                if min(ant, length-ant) > closestToMedian:
                    closestToMedian = min(ant, length-ant)

                if max(ant, length-ant) > farthestFromMedian:
                    farthestFromMedian = max(ant, length-ant)
            readAnts += len(newAnts)


        print(closestToMedian, end=" ")
        print(farthestFromMedian)




def main():
    ants()
main()
