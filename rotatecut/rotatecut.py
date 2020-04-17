import sys

def rotatecut(lines):
    numCases = int(lines[0].split(" ")[0])
    retString = []
    lines = lines[1:]

    for i in range(numCases):
        numRotates = int(lines[i].split(" ")[0])
        word = lines[i].split(" ")[1]

        while numRotates > 0:
            toBeRemovedLeft = len(word) // 4
            if toBeRemovedLeft == 0:
                break

            word = word[toBeRemovedLeft:]

            numRotates -= 1

            toBeRemovedRight = len(word) // 4
            if numRotates == 0 or toBeRemovedRight == 0:
                break

            word = word[:-toBeRemovedRight]
            numRotates -= 1

        retString.append(word)



    return "\n".join(retString)




def main():
    lines = [line.strip() for line in sys.stdin]
    print(rotatecut(lines))
main()
