import sys
import math

def yinyangstones(lines):
    stones = list(lines[0])
    print(stones)
    finished = False

    while not finished:
        finished = True
        for i in range(len(stones)):
            for j in range(i, len(stones)+i):
                print(stones)
                print(i, j)
                k = i+j % len(stones)

                result = check_for_legal_operation(i, j, stones)

                if result == "W":
                    del stones[i:k]

                    stones.insert(i, "W")
                    finished = False

                elif result == "B":
                    del stones[i:k]

                    stones.insert(i, "B")
                    finished = False
    print(stones)

def check_for_legal_operation(i, j, stones):
    if i == j:
        return None
    whites = 0
    blacks = 0
    for stone in range(i, j):
        ind = stone % len(stones)
        if stones[ind] == "W":
            whites += 1
        elif stones[ind] == "B":
            blacks += 1

    if abs(whites-blacks) == 1:
        return "W" if whites > blacks else "B"


def main():
    lines = [line.strip() for line in sys.stdin]
    print(yinyangstones(lines))
main()
