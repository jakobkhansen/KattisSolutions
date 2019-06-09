import sys

def coldputer(linjeArray):

    numTemp = int(linjeArray[0])
    temps = linjeArray[1].split(" ")
    temps = [int(i) for i in temps]

    return len([temp for temp in temps if temp < 0])

def main():

    linjer = [linje for linje in sys.stdin]

    print(coldputer(linjer))

main()
