import sys

def bus(lines):
    numCases = int(lines[0])

    for i in range(numCases):
        case = int(lines[i+1])
        passengers = 0

        for i in range(case):
            passengers += 0.5
            passengers *= 2
        print(int(passengers))


def main():
    lines = [line.strip() for line in sys.stdin]
    bus(lines)
main()
