import sys

# Bruk union-find datastructure for hver komponent for 0 og 1, for hver query sjekk om
# hver pos er i samme komponent

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

def valid_index(pos, r, c):
    x,y = pos

    return 0 <= x < r and 0 <= y < c

def location_to_index(x,y,c):
    return x*c + y

def find_sentinels(uf, world, r, c):
    for x,row in enumerate(world):
        for y,symbol in enumerate(row):
            right = (x,y+1)
            down = (x+1, y)
            if valid_index(right, r, c) and world[right[0]][right[1]] == symbol:
                uf.union(location_to_index(x,y,c), location_to_index(right[0], right[1], c))
            if valid_index(down, r, c) and world[down[0]][down[1]] == symbol:
                uf.union(location_to_index(x,y,c), location_to_index(down[0], down[1], c))

def process_queries(uf, world, c):

    sys.stdin.readline()
    for query in sys.stdin:
        x1,y1,x2,y2 = [int(x)-1 for x in query.split()]
        symbol = world[x1][y1]

        if uf.find(location_to_index(x1,y1,c)) == uf.find(location_to_index(x2,y2,c)):
            print('decimal' if symbol == '1' else 'binary')
        else:
            print('neither')



def tenkindsofpeople():
    r, c = [int(x) for x in sys.stdin.readline().split()]

    world = [list(sys.stdin.readline().strip()) for _ in range(r)]

    uf = UnionFind(r*c)

    find_sentinels(uf, world, r, c)

    process_queries(uf, world, c)


def main():
    tenkindsofpeople()
main()
