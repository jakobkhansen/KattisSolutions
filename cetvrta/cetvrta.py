import sys

def cetvrta(lines):
    left = []
    right = []
    retString = ""
    for line in lines:
        x,y = [int(x) for x in line.split()]
        left.append(x)
        right.append(y)

    seenLeft = set()
    for num in left:
        if num not in seenLeft:
            seenLeft.add(num)
        else:
            seenLeft.remove(num)
    retString += str(seenLeft.pop())

    seenRight = set()
    for num in right:
        if num not in seenRight:
            seenRight.add(num)
        else:
            seenRight.remove(num)
    retString += " {}".format(seenRight.pop())

    return retString


def main():
    lines = [line.strip() for line in sys.stdin]
    print(cetvrta(lines))
main()
