import sys
import math

def pyramids():
    n = int(input())

    res = math.floor(math.sqrt(math.sqrt(n)))

    return res if res % 2 == 1 else res-1



def main():
    print(pyramids())
main()
