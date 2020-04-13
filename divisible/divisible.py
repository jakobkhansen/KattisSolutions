import sys
import re

def divisible(lines):
    numTestCases = int(lines[0].split(" ")[0])
    leftIndex = 1

    for i in range(numTestCases):
        d = int(lines[leftIndex].split(" ")[0])
        leftIndex += 1

        array = [int(x) for x in lines[leftIndex].split(" ")]
        sums = precompute(array)
        print(bruteForce(array, sums, d))

        leftIndex += 1

def precompute(array):
    count = 0
    sums = []
    for i in array:
        count += i
        sums.append(count)

    return sums

def bruteForce(array, sums, d):
    count = 0
    remainder = [0]*len(array)
    countings = {}
    for i in range(len(array)):
        if (i == 0):
            remainder[i] = (array[i] % d)
        else:
            remainder[i] = ((remainder[i-1] + array[i]) % d)

        if remainder[i] == 0:
            countings[remainder[i]] = 1
        else:
            countings[remainder[i]] = 0
    print(remainder)
    print(countings)

    for i in range(len(array)):
        count += countings[remainder[i]]
        countings[remainder[i]] = countings[remainder[i]] + 1

    return count


def main():
    lines = list(sys.stdin)
    divisible(lines)
main()
