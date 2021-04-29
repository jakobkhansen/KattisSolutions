import sys
from functools import cmp_to_key
from queue import PriorityQueue

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

    def __lt__(self, other):
        p1 = self.severity + self.constant*(-self.arrival)
        p2 = other.severity + other.constant*(-other.arrival)

        if p1 == p2:
            return self.name < other.name

        return p1 > p2



def clinic():
    constant = int(sys.stdin.readline().split()[1])
    queue = PriorityQueue()
    people = {}
    for query in sys.stdin:
        type = query.split()[0]
        if type == '1':
            arrival(query, queue, constant, people)
        elif type == '2':
            treat(queue)
        elif type == '3':
            gone(query, people)


def arrival(query, queue, constant, people):
    _,t,m,s = query.split()
    person = Person(m,int(t),int(s), constant)
    queue.put(person)
    people[person.name] = person

def gone(query, people):
    _,t,m = query.split()
    if people.get(m, False):
        people.get(m).gone = True

def treat(queue):
    if queue.empty():
        print("doctor takes a break")
    else:
        curr = queue.get()
        while curr.gone and not queue.empty():
            curr = queue.get()
        print(curr.name)

def main():
    (clinic())
main()
