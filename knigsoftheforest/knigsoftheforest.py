import sys
from queue import PriorityQueue
import bisect

class Moose:
    def __init__(self, year, strength, karl):
        self.year = year
        self.strength = strength
        self.karl = karl

    def __lt__(self, other):
        return self.strength > other.strength

    def __repr__(self):
        return "{} {} {}".format(self.year, self.strength, self.karl)

def knigsoftheforest(lines):
    pool = []
    poolQueue = PriorityQueue()
    poolSize = int(lines[0].split(" ")[0])
    moose = []
    mooseYear = 2011

    karl = [int(x) for x in lines[1].split(" ")]
    karlObj = Moose(karl[0], karl[1], True)
    moose.append(karlObj)
    for line in lines[2:]:
        mooseNums = [int(x) for x in line.split(" ")]
        mooseObj = Moose(mooseNums[0], mooseNums[1], False)
        moose.append(mooseObj)

    moose.sort(key=lambda x: x.year)

    currentMoose = 0

    while currentMoose < len(moose):
        while moose[currentMoose].year == mooseYear:
            poolQueue.put(moose[currentMoose])
            currentMoose += 1

            if currentMoose >= len(moose):
                break

        if poolQueue.qsize() < poolSize:
            return "unknown"

        newAlpha = poolQueue.get()

        if newAlpha.karl:
            return mooseYear

        mooseYear += 1
    return "unknown"




def main():
    lines = [line.strip() for line in sys.stdin]
    print(knigsoftheforest(lines))
main()
