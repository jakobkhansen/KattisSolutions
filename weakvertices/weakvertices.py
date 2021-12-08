def weakvertices():
    num_nodes = int(input())
    while num_nodes != -1:
        weak = []
        matrix = [[int(x) for x in input().split(" ")] for _ in range(num_nodes)]
        # print(matrix)
        for i in range(len(matrix)):
            is_weak = True
            for j in range(len(matrix)):
                for k in range(len(matrix)):
                    if is_triangle(matrix, i, j, k):
                        is_weak = False
                        break
                if not is_weak:
                    break
            if is_weak:
                weak.append(i)
        print(" ".join([str(x) for x in weak]))
        num_nodes = int(input())

def is_triangle(matrix, i, j, k):
    return neighbours(matrix, i, j) and neighbours(matrix, i, k) and neighbours(matrix, j, k)

def neighbours(matrix, i, j):
    return matrix[i][j] == 1

weakvertices()

