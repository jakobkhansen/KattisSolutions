import sys

def islands3(lines):
    matrix = [[char for char in x] for x in lines[1:]]
    visited = [[False for _ in x] for x in matrix]
    min_islands = 0
    for i,row in enumerate(matrix):
        for j,cell in enumerate(row):
            if not visited[i][j] and matrix[i][j] == 'L':
                dfs(i,j,matrix,visited)
                min_islands += 1
    return min_islands

def dfs(x,y,matrix,visited):
    visited[x][y] = True

    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dir in directions:
        new_x,new_y = x+dir[0],y+dir[1]
        if new_x >= 0 and new_x < len(matrix) and new_y >= 0 and new_y < len(matrix[new_x]):
            if not visited[new_x][new_y] and matrix[new_x][new_y] != 'W':
                dfs(new_x, new_y, matrix, visited)




def main():
    lines = [line.strip() for line in sys.stdin]
    print(islands3(lines))
main()
