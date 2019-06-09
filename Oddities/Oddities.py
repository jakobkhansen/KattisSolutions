import sys

def oddOrEven(linje):
    if int(linje)%2 == 0:
        return linje + " is even"

    return linje + " is odd"


def main():
    linjer = [linje.strip() for linje in sys.stdin]

    for linje in linjer[1:]:
        print(oddOrEven(linje))

main()
