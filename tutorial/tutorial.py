import sys
import math

def tutorial(lines):
    complexities = {
        1:lambda x,y: fact(x,y),
        2:lambda x: 2 ** x,
        3:lambda x: x ** 4,
        4:lambda x: x ** 3,
        5:lambda x: x ** 2,
        6:lambda x: x * math.log2(x),
        7:lambda x: x
    }

    m,n,t = [int(x) for x in lines[0].split(" ")]

    if t == 1:
        return "AC" if complexities[t](m, n) <= m else "TLE"

    return "AC" if complexities[t](n) <= m else "TLE"

def fact(m,n):
    currentSum = 1

    for i in range(1,n+1):
        currentSum *= i

        if currentSum > m:
            return currentSum

    return currentSum






def main():
    lines = [line.strip() for line in sys.stdin]
    print(tutorial(lines))
main()
