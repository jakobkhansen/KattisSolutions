import sys

def skruop():
    curr = 7
    n = int(sys.stdin.readline())
    for line in sys.stdin:
        if line.strip().lower() == "skru op!":
            if curr < 10:
                curr += 1
        elif line.strip().lower() == "skru ned!":
            if curr > 0:
                curr -= 1
    return curr


print(skruop())
