import sys

def codetosavelives():
    n = int(input())
    for _ in range(n):
        num1 = int("".join(input().split()))
        num2 = int("".join(input().split()))
        print(" ".join(str(num1+num2)))


codetosavelives()
