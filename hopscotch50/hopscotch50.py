import sys

def hopscotch50():
    n,k = [int(x) for x in sys.stdin.readline().split()]
    map = [[int(x) for x in y.split()] for y in sys.stdin]

    # Locations of all 1's, 2's, etc
    locations = [[] for _ in range(k)]

    for x,row in enumerate(map):
        for y,val in enumerate(row):
            locations[val-1].append((x,y))

    for location in locations:
        if len(location) == 0:
            return -1


    memory = {}


    for location in locations[-1]:
        memory[location] = 0

    for i in range(len(locations)-2, -1, -1):
        for location in locations[i]:
            memory[location] = min([distance(location, x) + memory[x] for x in locations[i+1]])



    return min([memory[x] for x in locations[0]])

def distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


def main():
    print(hopscotch50())
main()
