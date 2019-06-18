import sys

def textureanalysis(lines):
    returnString = ""
    teller = 1
    for line in lines:
        if line == "END":
            break

        lineArray = []

        for char in range(len(line)):
            if (char != len(line) -1 and line[char] == "*"):
                index = char + 1
                numWhites = 0

                while (line[index] != "*"):
                    numWhites += 1
                    index += 1
                lineArray.append(numWhites)

        if (everyElemEqual(lineArray)):
            returnString += str(teller) + " EVEN\n"
        else:
            returnString += str(teller) + " NOT EVEN\n"

        teller += 1

    return returnString

def everyElemEqual(paramList):
    if (paramList == []):
        return True

    baseElem = paramList[0]
    for elem in paramList:
        if elem != baseElem:
            return False
    return True

def main():
    lines = [line.strip() for line in sys.stdin]
    print(textureanalysis(lines))
main()
