import sys


def classy(lines):

    t = int(lines[0].split(" ")[0])
    index = 1
    retString = ""
    for _ in range(t):
        numPeople = int(lines[index].split(" ")[0])
        index += 1
        people = {}
        for _ in range(numPeople):
            lineSplit = lines[index].split(" ")
            name = lineSplit[0][:-1]
            pClass = lineSplit[1]

            people[name] = pClass
            index += 1

        sortedString = sortPeople(people)
        sortedString += "\n" + "="*30

        retString += sortedString + "\n"

    return retString.strip()



def sortPeople(people):
    sortedString = []
    for person in people.keys():
        index = 0
        while index < len(sortedString):
            otherPerson = sortedString[index]
            if comparePeople(people, person, otherPerson):
                sortedString.insert(index, person)
                break
            index += 1

        if index >= len(sortedString):
            sortedString.append(person)

    return "\n".join(sortedString)

def comparePeople(people, person1, person2):
    classes = {
        "upper":3,
        "middle":2,
        "lower":1
    }

    p1class = people[person1].split("-")
    p2class = people[person2].split("-")

    p1index = len(p1class) - 1
    p2index = len(p2class) - 1

    while (p1index >= 0 and p2index >= 0):
        currentP1class = classes[p1class[p1index]]
        currentP2class = classes[p2class[p2index]]
        if (currentP1class < currentP2class):
            return False

        if (currentP1class > currentP2class):
            return True

        p1index -= 1
        p2index -= 1

    while (p1index >= 0):
        currentP1class = classes[p1class[p1index]]
        if (currentP1class < 2):
            return False

        if (currentP1class > 2):
            return True
        p1index -= 1

    while (p2index >= 0):
        currentP2class = classes[p2class[p2index]]
        if (currentP2class > 2):
            return False

        if (currentP2class < 2):
            return True
        p2index -= 1


    # Alphabetical
    if person1 < person2:
        return True

    return False


def main():
    lines = [line.strip() for line in sys.stdin]
    print(classy(lines))
main()
