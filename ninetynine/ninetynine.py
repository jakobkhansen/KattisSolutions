import sys
import random

def ninetynine():
    current = 1
    print(current, flush=True)
    for num in sys.stdin:
        current = int(num)
        if current % 3 == 0:
            current += random.randint(1,2)
        elif current % 3 == 1:
            current += 2
        elif current % 3 == 2:
            current += 1
        print(current, flush=True)


def main():
    (ninetynine())
main()
