import sys

def Bela(lines):
    dominant = {
        "A":11,
        "K":4,
        "Q":3,
        "J":20,
        "T":10,
        "9":14,
        "8":0,
        "7":0
    }
    nonDominant = {
        "A":11,
        "K":4,
        "Q":3,
        "J":2,
        "T":10,
        "9":0,
        "8":0,
        "7":0
    }

    dominantSuit = lines[0].split(" ")[1]

    returnSum = 0
    for line in lines[1:]:
        if line[1] == dominantSuit:
            returnSum += dominant[line[0]]
        else:
            returnSum += nonDominant[line[0]]
    return returnSum


def main():
    lines = [line.strip() for line in sys.stdin]

    print(Bela(lines))
main()
