import sys

def sevenwonders(lines):
    played = {
        "T": 0,
        "C": 0,
        "G": 0
    }

    for char in lines[0]:
        played[char] += 1

    power_sum = sum(map(lambda x:  played[x]**2, played.keys()))

    set_sum = min(map(lambda x: played[x], played.keys()))*7

    return power_sum + set_sum


def main():
    lines = [line.strip() for line in sys.stdin]
    print(sevenwonders(lines))
main()
