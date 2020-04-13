import sys

def symmetricorder(lines):
    setCount = 1
    retString = ""
    while lines != []:
        numNames = int(lines[0].split(" ")[0])

        names = lines[1:numNames+1]
        if names != []:
            retString += "SET {}\n".format(setCount)
            retString += sortSet(names)

        lines = lines[numNames + 1:]
        setCount += 1

    return retString.strip()

def sortSet(names):

    newNames = [""]*len(names)

    leftIndex = 0
    rightIndex = len(names) - 1
    for i in range(0, len(names), 2):
        newNames[leftIndex] = names[i]
        
        if (i + 1) < len(names):
            newNames[rightIndex] = names[i+1]

        leftIndex += 1
        rightIndex -= 1

    return "\n".join(newNames) + "\n"
        


def main():
    lines = [line.strip() for line in sys.stdin]
    print(symmetricorder(lines))
main()
