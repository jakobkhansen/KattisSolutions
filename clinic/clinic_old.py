import sys
from functools import cmp_to_key

class Person:
    def __init__(self, name, arrival, severity, constant):
        self.name = name
        self.arrival = arrival
        self.severity = severity
        self.gone = False
        self.constant = constant

    def get_priority(self, time):
        return self.severity + self.constant*(time - self.arrival)

    def __repr__(self) -> str:
        return "({}, {})".format(self.name, self.gone)

def compare(first, other, time):
    if first.gone:
        return 1
    elif other.gone:
        return -1

    p1 = first.get_priority(time)
    p2 = other.get_priority(time)

    if p1 == p2:
        if first.name < other.name:
            return 1
        return -1

    return p1 - p2


def clinic():
    constant = int(sys.stdin.readline().split()[1])
    queue = []
    people = {}
    for query in sys.stdin:
        type = query.split()[0]
        if type == '1':
            arrival(query, queue, constant, people)
        elif type == '2':
            time = int(query.split()[1])
            sort(queue, time)
            treat(queue)
        elif type == '3':
            gone(query, people)


def arrival(query, queue, constant, people):
    _,t,m,s = query.split()
    person = Person(m,int(t),int(s), constant)
    queue.append(person)
    people[person.name] = person

def gone(query, people):
    _,t,m = query.split()
    if people.get(m, False):
        people.get(m).gone = True

def sort(queue, time):
    queue.sort(key=cmp_to_key(lambda x,y:compare(x,y,time)))
    while len(queue) > 0 and queue[-1].gone == True:
        queue.pop()

def treat(queue):
    if len(queue) == 0:
        print("doctor takes a break")
    else:
        print(queue.pop().name)

def main():
    (clinic())
main()
