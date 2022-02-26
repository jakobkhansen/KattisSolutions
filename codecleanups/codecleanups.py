import sys

def codecleanups():
    n = int(input())
    days = {int(x):True for x in input().split()}

    dirtyness = 0
    numDirtyPushes = 0
    cleanups = 0

    for i in range(1, 366):
        if days.get(i, False):
            numDirtyPushes += 1
        dirtyness += numDirtyPushes

        if dirtyness >= 20:
            cleanups += 1
            numDirtyPushes = 0
            dirtyness = 0
    if dirtyness > 0:
        cleanups += 1

    return cleanups
        



def main():
    print(codecleanups())
main()
