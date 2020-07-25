import sys

def provincesandgold(lines):
    victory = [
        ["Province", 8],
        ["Duchy", 5],
        ["Estate", 2]
    ]

    treasure = [
        ["Gold", 6],
        ["Silver", 3],
        ["Copper", 0]
    ]

    gold,silver,copper = [int(x) for x in lines[0].split()]
    buyingpower = gold*3 + silver*2 + copper

    buy = []

    for victorycard in victory:
        if victorycard[1] <= buyingpower:
            buy.append(victorycard[0])
            break

    for treasurecard in treasure:
        if treasurecard[1] <= buyingpower:
            buy.append(treasurecard[0])
            break

    return " or ".join(buy)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(provincesandgold(lines))
main()
