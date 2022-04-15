import sys

def gcvwr():
    g,t,n = [int(x) for x in input().split()]
    items = [int(x) for x in input().split()]
    capacity = (g-t)*0.9
    for item in items:
        capacity -= item
    return int(capacity)

print(gcvwr())
