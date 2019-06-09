import sys

def tarifa(fileListe):

    mbLimit = fileListe[0]
    currentMb = 0


    for monthUse in fileListe[2:]:
        currentMb += fileListe[0] - monthUse

    currentMb += fileListe[0]
    return currentMb



def main():

    test = []

    for linje in sys.stdin:
        test.append(int(linje))

    print(tarifa(test))

main()

