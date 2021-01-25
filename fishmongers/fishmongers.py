import sys

def fishmongers(lines):
    fish = [int(x) for x in lines[1].split(" ")]
    mongers  = []

    for monger in lines[2:]:
        monger = [int(x) for x in monger.split(" ")]
        mongers.append(monger)

    mongers.sort(key=lambda x: x[1], reverse=True)
    fish.sort(reverse=True)


    currentFish = 0
    currentMonger = 0
    monies = 0

    while currentFish < len(fish) and currentMonger < len(mongers):
        while mongers[currentMonger][0] > 0:
            monies += mongers[currentMonger][1]*fish[currentFish]
            currentFish += 1
            mongers[currentMonger][0] -= 1

            if currentFish >= len(fish):
                break
        currentMonger += 1
    return monies



def main():
    lines = [line.strip() for line in sys.stdin]
    print(fishmongers(lines))
main()
