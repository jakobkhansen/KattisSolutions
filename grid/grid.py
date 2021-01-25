import sys
from queue import Queue

class Point:
    def __init__(self, spot, previous):
        self.spot = spot
        self.previous = previous

    def __repr__(self):
        return str(self.spot)

def grid(lines):
    n, m = [int(x) for x in lines[0].split(" ")]

    if n == 0 or m == 0:
        return -1

    if n == 1 and m == 1:
        return 0

    grid = []
    visited = []

    for i in range(1,n+1):
        row = [int(x) for x in lines[i]]
        visitedRow = [False for x in lines[i]]
        grid.append(row)
        visited.append(visitedRow)

    queue = Queue()

    start = Point((0,0), 0)
    visited[0][0] = True
    goal = (n-1,m-1)
    queue.put(start)

    while not queue.empty():
        current = queue.get()

        curSpot = current.spot
        moveVal = grid[curSpot[0]][curSpot[1]]

        if moveVal == 0:
            continue

        if not curSpot[0]-moveVal < 0:
            newPoint = Point((curSpot[0]-moveVal, curSpot[1]), current.previous+1)

            if newPoint.spot == goal:
                return current.previous+1

            if visited[newPoint.spot[0]][newPoint.spot[1]]:
                pass
            else:
                visited[newPoint.spot[0]][newPoint.spot[1]] = True
                queue.put(newPoint)

        if curSpot[0]+moveVal < len(grid):
            newPoint = Point((curSpot[0]+moveVal, curSpot[1]), current.previous+1)

            if newPoint.spot == goal:
                return current.previous+1

            if visited[newPoint.spot[0]][newPoint.spot[1]]:
                pass
            else:
                visited[newPoint.spot[0]][newPoint.spot[1]] = True
                queue.put(newPoint)

        if not curSpot[1]-moveVal < 0:
            newPoint = Point((curSpot[0], curSpot[1]-moveVal), current.previous+1)

            if newPoint.spot == goal:
                return current.previous+1

            if visited[newPoint.spot[0]][newPoint.spot[1]]:
                pass
            else:
                visited[newPoint.spot[0]][newPoint.spot[1]] = True
                queue.put(newPoint)

        if curSpot[1]+moveVal < len(grid[0]):
            newPoint = Point((curSpot[0], curSpot[1]+moveVal), current.previous+1)


            if newPoint.spot == goal:
                return current.previous+1

            if visited[newPoint.spot[0]][newPoint.spot[1]]:
                pass
            else:
                visited[newPoint.spot[0]][newPoint.spot[1]] = True
                queue.put(newPoint)

    return -1









def main():
    lines = [line.strip() for line in sys.stdin]
    print(grid(lines))
main()
