import sys

def numCarrots(linjer):
    return linjer[0].split(" ")[1]



def main():
    linjer = [linje.strip() for linje in sys.stdin]

    print(numCarrots(linjer))
main()
