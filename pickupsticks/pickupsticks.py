import sys

def pickupsticks(lines):
    n,m = [int(x) for x in lines[0].split()]
    inEdges = [0]*n

    edges = {x:[] for x in range(1, n+1)}

    for line in lines[1:]:
        a,b = [int(x) for x in line.split()]
        inEdges[b-1] += 1
        edges[a].append(b)

    queue = []

    for stick in edges.keys():
        if inEdges[stick-1] == 0:
            queue.append(stick)

    order = []
    processed = 0
    while len(queue) != 0:
        current = queue.pop()
        order.append(current)
        processed += 1

        for edge in edges[current]:
            inEdges[edge-1] -= 1
            if inEdges[edge-1] == 0:
                queue.append(edge)
    if processed < n:
        return "IMPOSSIBLE"
    
    return "\n".join([str(x) for x in order])





def main():
    lines = [line.strip() for line in sys.stdin]
    print(pickupsticks(lines))
main()
