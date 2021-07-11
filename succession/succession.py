import sys

class Person:
    """Hello"""
    name: str
    father: str or None
    mother: str or None

    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother



def succession(lines):
    people = {}
    n,m = [int(x) for x in lines[0].split()]
    king = lines[1]
    people[king] = Person(king, "", "")

    for i in range(n):
        child,father,mother = lines[i+2].split()
        people[child] = Person(child, father, mother)

    claimers = [people.get(x) for x in lines[n+2:]]
    blood_vals = [(x, get_blood_value(people, x)) for x in claimers]
    return max(blood_vals, key=lambda x: x[1])[0].name

def get_blood_value(people, person):
    if person is None:
        return 0
    if person.father is "" and person.mother is "":
        return 1

    father = people.get(person.father)
    mother = people.get(person.mother)
    father_blood = 0 if father is None else get_blood_value(people, father)
    mother_blood = 0 if mother is None else get_blood_value(people, mother)
    return (father_blood / 2) + (mother_blood / 2)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(succession(lines))
main()
