import sys
from queue import Queue

class Node:
    def __init__(self, name, exists=True):
        self.name = name
        self.paths = []
        self.visited = False
        self.previous = None
        self.exists = exists

    def __repr__(self) -> str:
        return f"Node({self.name}, {[x.name for x in self.paths]})"

def torn2pieces(lines):
    nodes = {}
    for line in lines[1:-1]:
        station = line.split()[0]
        nodes[station] = Node(station)

    for line in lines[1:-1]:
        node = nodes[line.split()[0]]
        for neighbour in line.split()[1:]:
            if not nodes.get(neighbour, False):
                nodes[neighbour] = Node(neighbour, False)

            node.paths.append(nodes[neighbour])

            if not nodes[neighbour].exists:
                nodes[neighbour].paths.append(node)

    start_node = nodes.get(lines[-1].split()[0], None)
    end_node = nodes.get(lines[-1].split()[1], None)
    # print(start_node)
    # print(end_node)
    if end_node == None or start_node == None:
        return 'no route found'

    dfs(start_node)

    if end_node.previous == None:
        return 'no route found'

    path = []

    current = end_node
    while current != None:
        path.append(current.name)
        current = current.previous

    return " ".join(reversed(path))


def dfs(node, previous=None):
    node.visited = True

    if previous != None:
        node.previous = previous

    for edge in node.paths:
        if not edge.visited:
            dfs(edge, node)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(torn2pieces(lines))
main()
