import sys

def conundrum(lines):
    cypher = "PER"
    inputStr = lines[0]

    numChanges = 0
    for i, char in enumerate(inputStr):
        if char != cypher[i % len(cypher)]:
            numChanges += 1

    return numChanges


def main():
    lines = [line.strip() for line in sys.stdin]
    print(conundrum(lines))
main()
