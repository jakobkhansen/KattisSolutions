import sys

class Node:
    def __init__(self, id):
        self.id = id
        self.edges = {}
        self.relax = sys.maxsize
        self.num_nodes_path = 1

    def addEdge(self, node, weight):
        self.edges[node] = weight

class PrioQueue:
    def __init__(self):
        self.queue = []

    def insert(self, node):
        self.queue.append(node)

    def pop(self):
        smallest = self.queue[0]
        smallest_index = 0

        for index, node in enumerate(self.queue):
            if node.relax < smallest.relax:
                smallest = node
                smallest_index = index
        return self.queue.pop(smallest_index)

    def isEmpty(self):
        return len(self.queue) == 0

    def contains(self, node):
        return node in self.queue


def shortestpath4():
    tc = int(sys.stdin.readline().split()[0])
    retString = ""

    for _ in range(tc):
        sys.stdin.readline()
        v = int(sys.stdin.readline().split()[0])

        nodes = []

        for i in range(v):
            nodes.append(Node(i))

        for nodeIndex in range(v):
            edgeLine = sys.stdin.readline().split()
            for i in range(1, len(edgeLine), 2):
                edge_index = int(edgeLine[i])
                edge_weight = int(edgeLine[i+1])
                nodes[nodeIndex].addEdge(nodes[edge_index], edge_weight)
        num_queries = int(sys.stdin.readline())
        retString += parseQueries(nodes, num_queries) + "\n"

    print(retString.strip())



def parseQueries(nodes, num_queries):
    retString = ""
    for _ in range(num_queries):
        query = [int(x) for x in sys.stdin.readline().split()]

        from_node = nodes[query[0]]
        to_node = nodes[query[1]]
        path_limit = query[2]


        best = [sys.maxsize]*len(nodes)
        best[from_node.id] = 0

        depth_limited_path(best, from_node, path_limit, 0, 0)

        retString += str(best[to_node.id]) + "\n"

    return retString

def buildGraphFromBFS(nodes, start_node, depth_limit):
    layers = []
    current_layer = 0
    layers.append([start_node])
    newgraph = []
    mapping = {}


    for node in nodes:
        newNode = Node(node.id)
        newgraph.append(newNode)
        mapping[node] = newNode

    while (current_layer < len(layers) and current_layer < depth_limit - 1):
        newLayer = []
        for node in layers[current_layer]:
           for edge in node.edges.keys():
               newLayer.append(edge)
               mapping[node].addEdge(mapping[edge], node.edges[edge])
        layers.append(newLayer)
        current_layer += 1

    return newgraph

def depth_limited_path(best, node, limit, length, cost):
    # print("node " + str(node.id))
    # print(cost)
    if length < limit:
        if cost < best[node.id]:
            # print("yes")
            # print(best[node.id])
            # print(cost)
            # print()
            best[node.id] = cost
    else:
        return
    for edge in node.edges.keys():
        # print("From " + str(node.id), end=" ")
        # print("To " + str(edge.id))
        depth_limited_path(best, edge, limit, length+1, cost + node.edges[edge])


def dijkstra(from_node, to_node, path_length_limit):
    from_node.relax = 0
    queue = PrioQueue()
    queue.insert(from_node)
    finished = []

    while not queue.isEmpty():
        current = queue.pop()
        finished.append(current)
        print("\n" + str(current.id))

        # if (current.num_nodes_path < path_length_limit):
        for edge in current.edges.keys():
            print(edge.id)
            if not edge in finished and current.relax + current.edges[edge] < edge.relax:
                edge.relax = current.relax + current.edges[edge]
                if not queue.contains(edge):
                    queue.insert(edge)

    if to_node.relax == sys.maxsize:
        return -1

    return to_node.relax


def reset_nodes(nodes):
    for node in nodes:
        node.relax = sys.maxsize
        node.num_nodes_path = 1



def printNodes(nodes):
    for node in nodes:
        print("Node: " + str(node.id))
        print("Relax value: " + str(node.relax))
        print("Path length: " + str(node.num_nodes_path))
        for edge in node.edges.keys():
            print("Edge to " + str(edge.id) + " with weight " + str(node.edges[edge]))
        print()


def test():
    nodes = []

    for i in range(7):
        nodes.append(Node(i))

    nodes[0].addEdge(nodes[1], 7)
    nodes[1].addEdge(nodes[4], 7)
    nodes[1].addEdge(nodes[5], 42)
    nodes[3].addEdge(nodes[2], 3)
    nodes[3].addEdge(nodes[5], 7)
    nodes[4].addEdge(nodes[6], 11)
    nodes[5].addEdge(nodes[6], 1)

    print(dijkstra(nodes, nodes[0], nodes[6], 4))
    # printNodes(nodes)



def main():
    shortestpath4()
main()
