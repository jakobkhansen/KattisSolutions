import sys

def awkwardparty(lines):
    
    people = [int(x) for x in lines[1].split(" ")]

    if not checkSimilar(people):
        return len(people)

    return determineAwkward(people)

def checkSimilar(people):
    languages = {}

    for person in people:
        if person in languages:
            return True

        languages[person] = 1

    return False

def determineAwkward(people):
    languages = [0]*(max(people) + 1)
    for i, person in enumerate(people):
        languages[person] = i - languages[person]

    return max(languages)

def main():
    lines = [line.strip() for line in sys.stdin]
    print(awkwardparty(lines))
main()
