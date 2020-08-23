import sys

def teque():
    commands = {
        "push_back":pushBack,
        "push_front":pushFront,
        "push_middle":pushMiddle,
        "get":get
    }

    left = []
    right = []

    sys.stdin.readline()

    for command in sys.stdin:
        commandSplit = command.split(" ")
        commandFunction = commands[commandSplit[0]]

        left, right = commandFunction(left, right, int(commandSplit[1]))




def pushBack(left, right, value):
    right.append(value)
    left, right = rearrange(left, right)
    return left, right

def pushFront(left, right, value):
    left.insert(0, value)
    left, right = rearrange(left, right)
    return left, right

def pushMiddle(left, right, value):
    if (len(left) >= len(right)):
        left.append(value)
    else:
        right.insert(1, value)

    left, right = rearrange(left, right)
    return left, right

def get(left, right, index):
    if (index < len(left)):
        print(left[index])
    else:
        print(right[index - len(left)])
    return left, right

def rearrange(left, right):
    if (abs(len(left) - len(right)) >= 2):
        middle = int((len(left) + len(right))/2)
        left.extend(right)

        newLeft = left[0:middle]
        newRight = left[middle:len(left)]


        return newLeft, newRight
    else:
        return left, right



def main():
    teque()
main()
