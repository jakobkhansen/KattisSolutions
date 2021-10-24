import sys

delta = {
    'N':(-1, 0),
    'S':(1, 0),
    'E':(0, 1),
    'W':(0, -1),
}

def treasurehunt(lines):
    r,c = [int(x) for x in lines[0].split()]
    map = [[x for x in y] for y in lines[1:]]
    start = (0,0)

    visited = set()
 
    def rec(pos):
        x,y = pos

        if pos in visited:
            raise Exception("Lost")
        visited.add(pos)

        if not ((0 <= x < r) and (0 <= y < c)):
            raise Exception("Out")

        if map[x][y] == 'T':
            return 0

        dx,dy = delta[map[x][y]]
        new_pos = x + dx, y + dy

        return 1 + rec(new_pos)

    try:
        return rec(start)
    except Exception as e:
        return str(e)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(treasurehunt(lines))
main()
