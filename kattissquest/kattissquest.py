import sys
from bisect import bisect_left, bisect_right, insort
from queue import PriorityQueue

class Quest:
    def __init__(self, energy, gold):
        self.energy = energy
        self.gold = gold

    def __lt__(self, other):
        if other == None:
            return False
        if self.energy == other.energy:
            return self.gold > other.gold
        return self.energy < other.energy


class EnergyClass:
    def __init__(self, energy):
        self.energy = energy
        self.quests = PriorityQueue()

    def __lt__(self, other):
        return self.energy < other.energy

    def __eq__(self, other):
        return self.energy == other.energy

def kattissquest():

    pool = []

    sys.stdin.readline()

    for command in sys.stdin:
        split = command.split(" ")
        if split[0] == "add":
            energy = int(split[1])
            gold = int(split[2])
            quest = Quest(int(energy), int(gold))

            energy_class = EnergyClass(energy)
            energy_index = index(pool, energy_class)

            if energy_index == None:
                insort(pool, energy_class)
                energy_class.quests.put(quest)
            else:
                pool[energy_index].quests.put(quest)
        elif split[0] == "query":
            query(pool, int(split[1]))


def query(pool, energy):
    gold = 0
    while energy > 0 and len(pool) > 0:
        search_class = EnergyClass(energy)

        search_index = find_le(pool, search_class)
        if search_index == None:
            break

        energy_class = pool[search_index]
        quest = energy_class.quests.get()

        if energy_class.quests.empty():
            pool.pop(search_index)

        energy -= quest.energy
        gold += quest.gold
    print(gold)


def find_le(a, x):
    i = bisect_right(a, x)
    if i:
        return i-1
    return None

def index(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None


def main():
    (kattissquest())
main()
