import sys

def zebrasocelots(lines):
    pile = [1 if x == 'Z' else 0 for x in lines[1:]]

    numRounds = 0

    vals = [
        1,
        2,
        3,
    ]

    for i,x in enumerate(reversed(pile)):
        # print(i, x)
        if x == 0:
            addedVal = i*i
            # print(addedVal)
            numRounds += addedVal



    return numRounds



def main():
    lines = [line.strip() for line in sys.stdin]
    print(zebrasocelots(lines))
main()
