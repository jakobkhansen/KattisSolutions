import sys

def forests(lines):
    people = {}
    opinions = {}

    numPeople = int(lines[0].split(" ")[0])

    for line in lines[1:]:
        spl = line.split(" ")
        person = int(spl[0])
        tree = int(spl[1])

        newList = people.get(person, [])
        newList.append(tree)
        people[person] = newList

    sortedVals = [sorted(x) for x in people.values()]
    # print(sortedVals)
    opinions = list(map(list, set(map(lambda i: tuple(i), sortedVals))))

    if len(people.keys()) < numPeople:
        return len(opinions) + 1

    return len(opinions)

    # return len(list(set(tuple(x)) for x in people.values()))
    # for personOpinion in people.values():
        # opinions[" ".join([str(x) for x in sorted(personOpinion)])] = True

    # return len(opinions.keys())




def main():
    lines = [line.strip() for line in sys.stdin]
    print(forests(lines))
main()
