import sys


def theplank():
    plank = int(input())
    return recur(plank)


def recur(left: int):
    if left == 0:
        return 1

    if left < 0:
        return 0

    return (recur(left - 1) + recur(left - 2) + recur(left - 3))


print(theplank())
