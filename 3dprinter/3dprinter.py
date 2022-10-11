import sys
import math

def threedprinter():
    n = int(input())
    printers = 1
    best = n

    for i in range(n):
        printers = 2**i
        numdays =int(n / printers) + bool(n%2) + i
        best = min(best, numdays)
    return best



print(threedprinter())
