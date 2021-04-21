import sys

def floodit(lines):
    cases = int(lines[0])

    index = 1
    for i in range(cases):
        sizeX = int(lines[index])
        sizeY = len(lines[index+1])
        index += 1
        map = []

        for j in range(sizeX):
            map.append([int(x) for x in lines[index+j]])

        visited = []

        for i in range(sizeX):
            ne = []
            for j in range(sizeY):
                ne.append(False)
            visited.append(ne)

        print(map)
        print(visited)

        countSurroundingOfNum(map, visited, 3, 3, 0, 0)

        print()



        index += sizeX


def countSurroundingOfNum(map, visited, currentNum, newNum, i, j):
    print(i, j)
    visited[i][j] = True

    localCount = 0
    for x,y in [[-1, 0], [1,0], [0,-1], [0,1]]:
        if map[x][y] == currentNum and not visited[x][y]:
            localCount += countSurroundingOfNum(map, visited, currentNum, newNum, x, y)
        elif map[x][y] == newNum and not visited[x][y]:
            visited[x][y] = True
            localCount += 1

    return localCount

def setSurroundingToNum(map, oldNum, newNum, i, j):
    map[i][j] = newNum
    for x,y in [[-1, 0], [1,0], [0,-1], [0,1]]:
        if map[x,y] == oldNum:
            setSurroundingToNum(map, oldNum, newNum, i, j)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(floodit(lines))
main()
