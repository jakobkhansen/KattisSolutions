import sys

def scalingrecipe():
    n,x,y = [int(x) for x in input().split()]
    scale = y/x
    for ingredient in sys.stdin:
        print(round(int(ingredient)*scale))

scalingrecipe()
