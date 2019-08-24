import sys

def zagrade(lines):
    expression = lines[0]
    print(expression)

    numBraces = expression.count("(")
    innerLeftBrace = findNth(expression, numBraces, "(")
    innerRightBrace = findNth(expression, 1, ")")
    print(innerRightBrace)
    print(removeBrace(expression, innerLeftBrace, innerRightBrace))


def findNth(expression, n, findChar):
    counter = 1
    for charIndex in range(len(expression)):
        if expression[charIndex] == findChar:
            if counter == n:
                return charIndex
            else:
                counter += 1
    return -1

def removeBrace(expression, leftBrace, rightBrace):
    returnString = expression
    returnString = returnString[:leftBrace] + returnString[leftBrace+1:]
    returnString = returnString[:rightBrace-1] + returnString[rightBrace:]
    return returnString


def main():
    lines = [line.strip() for line in sys.stdin]
    print(zagrade(lines))
main()
