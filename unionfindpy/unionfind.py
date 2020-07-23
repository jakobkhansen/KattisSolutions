import sys

def unionfind(lines):
    setNum = int(lines[0].split(" ")[0])
    unionData = [-1]*setNum
    return commandLoop(unionData, lines[1:]).strip()

def commandLoop(unionData, lines):
    retString = ""
    for line in lines:
        line_split = line.split(" ")

        symbol = line_split[0]

        num1 = int(line_split[1])
        num2 = int(line_split[2])

        if symbol == "?":
            retString += checkUnion(unionData, num1, num2) + "\n"
        elif symbol == "=":
            performUnion(unionData, num1, num2)
    return retString


def findParent(unionData, num):
    if unionData[num] < 0:
        return num
    current = num
    while unionData[current] >= 0:
        print(unionData)
        current = unionData[current]

    unionData[num] = current

    return current

def performUnion(unionData, num1, num2):
    parent1 = findParent(unionData, num1)
    parent2 = findParent(unionData, num2)

    unionData[parent1] = parent2

def checkUnion(unionData, num1, num2):
    if num1 == num2 or findParent(unionData, num1) == findParent(unionData, num2):
        return "yes"

    return "no"

def main():
    lines = [line.strip() for line in sys.stdin]
    print(unionfind(lines))
main()
