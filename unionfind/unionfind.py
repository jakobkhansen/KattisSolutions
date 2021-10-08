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
                self.array[a_parent] -= size_b
            else:
                self.array[a_parent] = b_parent
                self.array[b_parent] -= size_a

def main():
    n,q = [int(x) for x in sys.stdin.readline().split()]
    uf = UnionFind(n)

    for query in sys.stdin:
        query = query.split()
        a, b = int(query[1]),int(query[2])

        if query[0] == '?':
            result = 'yes' if uf.find(a) == uf.find(b) else 'no'
            print(result)
        else:
            uf.union(a, b)
main()

