import sys

def whichisgreater():
    a,b = [int(x) for x in input().split()]
    return 1 if a > b else 0

print(whichisgreater())
