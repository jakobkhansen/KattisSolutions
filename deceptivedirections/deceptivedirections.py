import sys
from collections import deque

movement = {
    'N':(-1,0),
    'S':(1,0),
    'W':(0,-1),
    'E':(0,1),
}

def deceptivedirections(lines):

        map = [list(x) for x in lines[1:-1]]

        directions = list(lines[-1])

        start = (0,0)

        for i,row in enumerate(map):
            for j,val in enumerate(row):
                if val == 'S':
                    start = (i,j)

        possible_spots = []

        queue = deque()
        visited = set()
        distances = {start: 0}

        queue.append(start)
        visited.add(start)

        while len(queue) > 0:
            current = queue.popleft()
            
            if distances[current] >= len(directions):
                continue

            for dx,dy in movement.values():
                x,y = (current[0] + dx, current[1] + dy)

                if map[x][y] != '#' and (x,y) not in visited:
                    distances[(x,y)] = distances[current] + 1
                    visited.add((x,y))
                    queue.append((x,y))

        queue = deque()
        visited = set()

        queue.append(start)
        visited.add(start)

        while len(queue) > 0:
            current = queue.popleft()

            if distances[current] >= len(directions):
                possible_spots.append(current)
                continue 

            for move,(dx,dy) in movement.items():
                x,y = (current[0] + dx, current[1] + dy)

                if (x,y) in visited:
                    continue

                if map[x][y] == '#':
                    continue

                if distances[(x,y)] != distances[current] + 1:
                    continue

                if directions[distances[(x,y)]-1] != move:
                    visited.add((x,y))
                    queue.append((x,y))



        for x,y in possible_spots:
            map[x][y] = '!'

        return '\n'.join([''.join(x) for x in map])



def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])




def main():
    lines = [line.strip() for line in sys.stdin]
    print(deceptivedirections(lines))
main()
