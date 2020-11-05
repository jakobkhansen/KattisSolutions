import sys

def cudoviste(lines):
    retStr = []
    x,y = [int(x) for x in lines[0].split(" ")]

    grid = [list(x) for x in lines[1:]]
    # print(grid)
    parkingSpots = [0]*5

    for i in range(x-1):
        for j in range(y-1):
            spot = ['']*4
            spot[0] = grid[i][j]
            spot[1] = grid[i][j+1]
            spot[2] = grid[i+1][j]
            spot[3] = grid[i+1][j+1]

            if "#" in spot:
                continue
            parkingSpots[spot.count("X")] += 1

    return "\n".join([str(x) for x in parkingSpots])





def main():
    lines = [line.strip() for line in sys.stdin]
    print(cudoviste(lines))
main()
