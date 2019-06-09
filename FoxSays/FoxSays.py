import sys

def FoxSays(filLinjer):
    numCases = int(filLinjer[0])
    returnString = ""
    for cases in filLinjer[1:numCases+1]:
        foxSaying = cases.split()
        for saying in filLinjer[numCases+1:-1]:
            currentWord = saying.split()[-1]
            foxSaying = [word for word in foxSaying if word != currentWord]
        returnString += " ".join(foxSaying).strip()+"\n"
    return returnString.strip()

def main():

    linjer = [linje.strip() for linje in sys.stdin]
    print(FoxSays(linjer))

main()
