import sys
import math

def unlockpattern():
    locations = {}
    for i in range(3):
        line = input().split()
        for j in range(3):
            locations[int(line[j])] = (i,j)

    
    distance = 0
    for i in range(2,10):
        x1,y1 = locations[i-1]
        x2,y2 = locations[i]
        distance += math.sqrt((x2-x1)**2 + (y2 - y1)**2)
    return distance

print(unlockpattern())
