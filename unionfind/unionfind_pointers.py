import sys

class Node:
    def __init__(self, label, parent=None) -> None:
        self.label = label
        self.parent = parent
        self.size = 1


def find(node):
    root = node
    while root.parent != None:
        root = root.parent

    current = node
    while current.parent != None:
        old_parent = current.parent
        current.parent = root
        current = old_parent
    return root


def union(a, b):
    if a == b:
        return

    a_parent = find(a)
    b_parent = find(b)

    if a_parent == b_parent:
        return

    if a_parent.size >= b_parent.size:
        b_parent.parent = a_parent
        a_parent.size += b_parent.size
    else:
        a_parent.parent = b_parent
        b_parent.size += a_parent.size


def main():
    n,q = [int(x) for x in sys.stdin.readline().split()]
    nodes = {}

    for query in sys.stdin:
        query = query.split()
        a, b = query[1],query[2]

        if a not in nodes:
            nodes[a] = Node(a)
        if b not in nodes:
            nodes[b] = Node(b)

        if query[0] == '?':
            result = 'yes' if find(nodes[a]) == find(nodes[b]) else 'no'
            print(result)
        else:
            union(nodes[a], nodes[b])

main()
