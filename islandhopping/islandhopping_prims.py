import math
from heapq import heappop, heappush


def distance(p1, p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

def prims(positions):
    visited = set()
    s = positions[0]
    pq = []
    heappush(pq, (0,s))

    tree_sum = 0

    while pq and len(visited) < len(positions):
        # curr = pq.get()
        w,v = heappop(pq)
        if v in visited:
            continue

        visited.add(v)
        tree_sum += w

        for u in positions:
            if u != v and u not in visited:
                heappush(pq, (distance(u,v), u))
    return tree_sum

def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        positions = []
        for _ in range(m):
            positions.append(tuple([float(x) for x in input().split()]))
        print(prims(positions))

main()
