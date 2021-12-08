import sys
from collections import deque

class Person:
    def __init__(self, label, balance) -> None:
        self.label = label
        self.balance = balance
        self.friends = []

    def __repr__(self) -> str:
        return f'Person({self.label}, {self.balance}, {[x.label for x in self.friends]})'

def moneymatters():
    n,m = map(int, input().split())
    people = {}

    for i in range(n):
        people[i] = (Person(i, int(input())))

    for i in range(m):
        x,y = map(int, input().split())
        people[x].friends.append(people[y])
        people[y].friends.append(people[x])

    visited = set()

    for person in people.values():
        if person not in visited and not check_zero_bfs(person, visited):
            return "IMPOSSIBLE"
    
    return "POSSIBLE"


def check_zero_bfs(start, visited):
    queue = deque()
    queue.appendleft(start)
    visited.add(start)

    component_sum = 0

    while len(queue) > 0:
        current = queue.pop()
        # print(current)

        component_sum += current.balance
        # print(component_sum)

        for friend in current.friends:
            if friend not in visited:
                visited.add(friend)
                queue.appendleft(friend)
    return component_sum == 0

def main():
    print(moneymatters())
main()
