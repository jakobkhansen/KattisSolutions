import sys
from heapq import heapify, heappush, heappop


def vegetables():
    t, n = map(float, input().split())
    pq = []
    [heappush(pq, -float(x)) for x in input().split()]
    smallest = -max(pq)

    cuts = 0


    while ratio(smallest, -pq[0]) <= t:
        # print(ratio(smallest, -pq[0]))

        # print(ratio(smallest, -pq[0]))
        # print(smallest, -pq[0])
        # print(pq)
        print(pq)
        current = -heappop(pq)
        # print(current)
        # print(current)
        w_left = current / 2
        w_right = current / 2

        heappush(pq, -w_left)
        heappush(pq, -w_right)

        smallest = min(smallest, current / 2)

        cuts += 1
    print(cuts)


def ratio(smallest, largest):
    return smallest / largest


vegetables()
