import sys
import bisect

def grandpabernie(lines):
    numTrips = int(lines[0])
    trips = {}

    for tripStr in lines[1:numTrips+1]:
        spl = tripStr.split(" ")
        place = spl[0]
        year = int(spl[1])
        newList = trips.get(place, [])
        bisect.insort(newList, year)
        trips[place] = newList

    ret = []
    for queryStr in lines[numTrips+2:]:
        spl = queryStr.split(" ")
        place = spl[0]
        kth = int(spl[1])

        ret.append(str(trips[place][kth-1]))
    return "\n".join(ret)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(grandpabernie(lines))
main()
