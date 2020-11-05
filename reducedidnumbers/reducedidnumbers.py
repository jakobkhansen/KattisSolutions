import sys

def reducedidnumbers(lines):
    m = 1
    ids = [int(x) for x in lines[1:]]
    while True:
        alreadySeen = {}
        fucked = False
        for currId in ids:
            if alreadySeen.get(currId % m, False) == True:
                fucked = True
                break
            else:
                alreadySeen[currId % m] = True

        if not fucked:
            return m

        m += 1




def main():
    lines = [line.strip() for line in sys.stdin]
    print(reducedidnumbers(lines))
main()
