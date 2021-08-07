import sys

def findthegraph():
    num_nodes = int(input())
    matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                print(f"? 2 {i} {j}", flush=True)
                answer = int(input())
                if answer == 1:
                    matrix[i][j] = 1
    print(matrix)

def toString(matrix):
    pass


def main():
    findthegraph()
main()
