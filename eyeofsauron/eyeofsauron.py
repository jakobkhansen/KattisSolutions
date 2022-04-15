import sys

def eyeofsauron():
    tower = input()
    if len(tower) % 2 != 0:
        return 'fix'

    mid = len(tower) // 2
    return 'correct' if tower[mid-1] == '(' and tower[mid] == ')' else 'fix'

print(eyeofsauron())
