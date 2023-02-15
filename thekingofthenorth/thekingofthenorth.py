import sys

deltas = [(-1,0), (1,0), (0,-1), (0,1)]
r,c = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(r)]
c_x,c_y = [int(x) for x in input().split()]
cycles = [[] for i in range(r*c)]

def thekingofthenorth():
    print(r,c)
    print(matrix)
    for i in range(r):
        for j in range(c):
            dfs((i,j), set(), (i,j))
def dfs(location, visited, start):  
    x,y = location
    if ((x,y) in visited):  
        if ((x,y) == start):  
            "found a path"  
        return;  
    visited.add((x,y))
    for neighbour in get_adj(x,y):  
        dfs(neighbour,visited,start)
    visited.discard((x,y));
def get_adj(x,y):
    adj = []
    for xoff,yoff in deltas:
        n_x,n_y = x + xoff, y + yoff
        if verify_pos(n_x,n_y):
            adj.append((n_x, n_y))
    return adj
def verify_pos(x,y):
    return x >= 0 and x <= r and y >= 0 and y <= c


thekingofthenorth()
