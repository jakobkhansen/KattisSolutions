import sys

def alphabetspam(lines):
    inpStr = lines[0]
    inpLen = len(inpStr)

    numWhite = 0
    numLower = 0
    numUpper = 0
    numSymbols = 0

    for char in inpStr:
        if char == "_":
            numWhite += 1
        elif char.islower():
            numLower += 1
        elif char.isupper():
            numUpper += 1
        else:
            numSymbols += 1

    result = [numWhite/inpLen, numLower/inpLen, numUpper/inpLen, numSymbols/inpLen]

    return "\n".join([str(x) for x in result])



def main():
    lines = [line.strip() for line in sys.stdin]
    print(alphabetspam(lines))
main()
