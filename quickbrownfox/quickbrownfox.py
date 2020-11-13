import sys
import string

def quickbrownfox(lines):

    alpha = list(string.ascii_lowercase)

    numCases = int(lines[0])

    retStr = []

    for i in range(1, numCases+1):
        line = lines[i].lower()
        foundList = {}

        for char in alpha:
            foundList[char] = False

        for char in line:
            foundList[char] = True

        if all(value == True for value in foundList.values()):
            retStr.append("pangram")
        else:
            caseStr = "missing "
            for char in foundList.keys():
                if foundList[char] == False:
                    caseStr += char
            retStr.append(caseStr)

    return "\n".join(retStr)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(quickbrownfox(lines))
main()
