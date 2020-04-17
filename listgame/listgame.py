import sys
import math

def listgame(lines):
    num = int(lines[0].split(" ")[0])
    return str(primefactors(num))

def primefactors(n):
    primecount = 0
    while n % 2 == 0:
        primecount += 1
        n = n/2

    for i in range(3, int(math.sqrt(n))+1,2):

        while n % i == 0:
            primecount += 1
            n = n/i

    if n > 2:
        primecount += 1

    primecount




def main():
    lines = [line.strip() for line in sys.stdin]
    print(listgame(lines))
main()
