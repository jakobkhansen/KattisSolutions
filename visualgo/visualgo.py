from queue import PriorityQueue
import sys

class Node:
    def __init__(self, index) -> None:
        self.index = index
        self.edges = []
        self.relax = sys.maxsize
        self.paths = 0
        self.inqueue = False

    def __repr__(self):
        return f"Node({self.index}, {self.paths}, {[(x[0].index, x[1]) for x in self.edges]})"

    def __lt__(self, other):
        return self.relax < other.relax

def visualgo(lines):
    v,e = [int(x) for x in lines[0].split()]
    pqueue = PriorityQueue()
    nodes = []

    for i in range(v):
        nodes.append(Node(i))

    for edge in lines[1:-1]:
        n1, n2, w = [int(x) for x in edge.split()]
        nodes[n1].edges.append((nodes[n2], w))

    s,t = [int(x) for x in lines[-1].split()]
    nodes[s].relax = 0
    nodes[s].paths = 1

    pqueue.put(nodes[s])
    nodes[s].inqueue = True

    while not pqueue.empty():
        current = pqueue.get()
        current.inqueue = False
        for edge in current.edges:
            node, weight = edge
            if node.relax > current.relax + weight:
                node.relax = current.relax + weight
                node.paths = current.paths
                if not node.inqueue:
                    pqueue.put(node)
                    node.inqueue = True
            elif node.relax == current.relax + weight:
                node.paths += current.paths

    return nodes[t].paths






def main():
    lines = [line.strip() for line in sys.stdin]
    print(visualgo(lines))
main()
