import sys
from itertools import chain, combinations

def fridge(lines):
    digits = sorted([int(x) for x in lines[0]])


    subsets = subset(digits)
    next(subsets)
    prev = 0
    try:
        while True:
            curr_subset = next(subsets)
            number = sum(curr_subset)
            print(curr_subset)
            if number < prev or number > prev + 1:
                if prev + 1 < 1:
                    return 1
                return prev + 1
            prev = number
    except Exception:
        return 1
        
def sum(subset):
    num = 0
    multiplier = 1
    while subset[0] == 0:
        subset = subset[1:]
    for i in subset:
        num += i*multiplier
        multiplier *= 10
    return num

def subset(digits):
    for cardinality in range(len(digits) + 1):
        yield from combinations(digits, cardinality)

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def append_number(num, append):
    return int(str(num) + str(append))


def get_digit(num, pos):
    return num // 10**pos % 10

def num_positions(num):
    pos = 1
    current = num
    while current >= 10:
        current /= 10
        pos += 1
    return pos
    



def main():
    lines = [line.strip() for line in sys.stdin]
    print(fridge(lines))
main()
