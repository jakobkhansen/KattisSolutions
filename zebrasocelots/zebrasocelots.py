import sys

def zebrasocelots(lines):
    pile = [1 if x == 'Z' else 0 for x in lines[1:]]

    numRounds = 0

    for i,x in enumerate(reversed(pile)):
        if x == 0:
            addedVal = 2**i
            numRounds += addedVal



    return numRounds



def main():
    lines = [line.strip() for line in sys.stdin]
    print(zebrasocelots(lines))
main()
