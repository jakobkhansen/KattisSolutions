import sys

def kornislav():
    lens = [int(x) for x in input().split()]
    lens.sort()
    return lens[0]*lens[2]

print(kornislav())
