import math
from queue import PriorityQueue
import sys

class UnionFind:
    def __init__(self, n) -> None:
        self.array = [-1]*n

    def find(self, node):
        root = node
        while self.array[root] >= 0:
            root = self.array[root]

        current = node
        while self.array[current] >= 0:
            old_parent = self.array[current]
            self.array[current] = root
            current = old_parent

        return root

    def union(self, a, b):
        a_parent = self.find(a)
        b_parent = self.find(b)

        if a_parent != b_parent:
            size_a = -self.array[a_parent]
            size_b = -self.array[b_parent]

            if size_a >= size_b:
                self.array[b_parent] = a_parent
                self.array[a_parent] = -max(size_b+1, size_a)
            else:
                self.array[a_parent] = b_parent
                self.array[b_parent] = -max(size_a+1, size_b)

    def __len__(self):
        return len(self.array)

    def __repr__(self):
        return str(self.array)


def kruskals(m,positions):
    uf = UnionFind(m)
    mapping = {positions[x]:x for x in range(m)}
    pq = PriorityQueue()

    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            p1 = positions[i]
            p2 = positions[j]
            pq.put((distance(p1,p2), (p1,p2)))

    distance_sum = 0
    num_edges = 0

    while num_edges < m-1:
        dist,(p1,p2) = pq.get()
        if uf.find(mapping[p1]) != uf.find(mapping[p2]):
            distance_sum += dist
            num_edges += 1
            uf.union(mapping[p1], mapping[p2])
    print(distance_sum)
            




def distance(p1, p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

def main():
    n = int(input())
    for i in range(n):
        m = int(input())
        positions = []
        for j in range(m):
            positions.append(tuple([float(x) for x in input().split()]))
        kruskals(m,positions)
main()
