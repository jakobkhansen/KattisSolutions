import sys

def boatparts(lines):
    numParts = int(lines[0].split(" ")[0])
    parts = {}

    for i,line in enumerate(lines[1:]):
        parts[line] = True

        if len(parts.keys()) == numParts:
            return i+1
    return "paradox avoided"


def main():
    lines = [line.strip() for line in sys.stdin]
    print(boatparts(lines))
main()
