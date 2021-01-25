import sys

def synchronizinglists():
    n = int(sys.stdin.readline())

    while n != 0:

        firstList = []
        secondList = []

        for i in range(n):
            firstList.append(int(sys.stdin.readline()))

        for i in range(n):
            secondList.append(int(sys.stdin.readline()))

        firstSorted = sorted(firstList)
        secondSorted = sorted(secondList)

        correspondence = {}

        for i in range(n):
            correspondence[firstSorted[i]] = secondSorted[i]

        for i in range(n):
            print(correspondence[firstList[i]])

        n = int(sys.stdin.readline())

        if n == 0:
            break

        print()





def main():
    synchronizinglists()
main()
