import sys

def findQuadrant(linjer):
    x = int(linjer[0])
    y = int (linjer[1])

    if x < 0:
        if y < 0:
            return 3
        return 2

    else:
        if y < 0:
            return 4
        return 1



def main():
    linjer = [linjer for linjer in sys.stdin]

    print(findQuadrant(linjer))
main()
