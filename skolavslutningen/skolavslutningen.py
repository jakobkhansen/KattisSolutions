import sys

def skolavslutningen():
    n,m,k = [int(x) for x in input().split()]
    matrix = [[x for x in input()] for _ in range(n)]

    assigned = set()
    colors = 0

    for i in range(m):
        column_assigned = False
        for j in range(n):
            if matrix[j][i] in assigned:
                column_assigned = True
                break
        if not column_assigned:
            colors += 1
        for j in range(n):
            assigned.add(matrix[j][i])
    return colors


def main():
    print(skolavslutningen())
main()
