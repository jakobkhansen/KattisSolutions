import sys

currentExpression = None
currentToken = 0
currentCase = 0

def polish(expression):
    global currentExpression
    global currentToken
    global currentCase
    currentExpression = expression
    currentToken = 0
    currentCase += 1

    print("Case {}: {}".format(currentCase, parseExpression()))

def parseExpression():
    token = readToken()

    if (isInt(token)):
        return int(token)
    elif (token in ["+", "-", "*"]):
        left = parseExpression()
        right = parseExpression()

        if (isinstance(left, int) and isinstance(right, int)):
            return eval("{} {} {}".format(left, token, right))
        else:
            return "{} {} {}".format(token, left, right)
    else:
        return token

def isInt(token):
    try:
        int(token)
        return True
    except ValueError:
        return False

def readToken():
    global currentToken

    token = currentExpression.split(" ")[currentToken]
    currentToken += 1

    return token


def main():
    lines = [line.strip() for line in sys.stdin]
    for line in lines:
        polish(line)
main()
