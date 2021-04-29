import sys
from functools import cmp_to_key

class Player:
    def __init__(self, name, x, y, z):
        self.name = name
        self.skills = [x,y,z]
        self.used = False

    def compare(self, other, skill):
        if self.skills[skill] == other.skills[skill]:
            return ord(self.name) - ord(other.name)
        return self.skills[skill] - other.skills[skill]
    def __repr__(self):
        return "{}, {}, {}".format(self.name, self.skills, self.used)

def raidteams(lines):
    players = []
    for line in lines[1:]:
        n,x,y,z = line.split()
        players.append(Player(n,int(x), int(y), int(z)))

    arr1 = sorted(players, key=cmp_to_key(lambda x,y:compare_players(x,y,0)), reverse=True)
    arr2 = sorted(players, key=cmp_to_key(lambda x,y:compare_players(x,y,1)), reverse=True)
    arr3 = sorted(players, key=cmp_to_key(lambda x,y:compare_players(x,y,2)), reverse=True)

    # print(arr1)
    # print(arr2)
    # print(arr3)
    i1 = 0
    i2 = 0
    i3 = 0

    while i1 < len(arr1) and i2 < len(arr2) and i3 < len(arr3):
        party = []
        while i1 < len(arr1) and arr1[i1].used:
            i1 += 1

        if i1 >= len(arr1):
            break

        party.append(arr1[i1].name)
        arr1[i1].used = True

        while i2 < len(arr2) and arr2[i2].used:
            i2 += 1

        if i2 >= len(arr2):
            break

        party.append(arr2[i2].name)
        arr2[i2].used = True

        while i3 < len(arr3) and arr3[i3].used:
            i3 += 1

        if i3 >= len(arr3):
            break

        party.append(arr3[i3].name)
        arr3[i3].used = True

        print(" ".join(sorted(party)))




def compare_players(first, other, skill):
    if first.skills[skill] == other.skills[skill]:
        if first.name < other.name:
            return 1
        return -1
    return first.skills[skill] - other.skills[skill]



def main():
    lines = [line.strip() for line in sys.stdin]
    (raidteams(lines))
main()
