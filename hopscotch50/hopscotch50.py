import sys

def hopscotch50():
    n,k = [int(x) for x in sys.stdin.readline().split()]
    map = [[int(x) for x in y.split()] for y in sys.stdin]

    # Locations of all 1's, 2's, etc
    locations = [[] for _ in range(k)]

    for x,row in enumerate(map):
        for y,val in enumerate(row):
            locations[val-1].append((x,y))

    for location in locations:
        if len(location) == 0:
            return -1

    shortest = sys.maxsize

    def rec(index, current_pos, path_length):
        nonlocal shortest

        if index == k:
            if path_length < shortest:
                shortest = path_length
            return
        next_locations = locations[index]
        for next_pos in next_locations:
            new_distance = path_length + distance(current_pos, next_pos)
            if new_distance < shortest:
                rec(index+1, next_pos, new_distance)


    for start_pos in locations[0]:
        rec(1, start_pos, 0)
        if shortest == k:
            break

    return shortest

def distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


def main():
    print(hopscotch50())
main()
