import sys


def cprnummer():
    cpr = input()
    c1 = int(cpr[0])
    c2 = int(cpr[1])
    c3 = int(cpr[2])
    c4 = int(cpr[3])
    c5 = int(cpr[4])
    c6 = int(cpr[5])
    c7 = int(cpr[7])
    c8 = int(cpr[8])
    c9 = int(cpr[9])
    c10 = int(cpr[10])

    res = 4 * c1 + 3 * c2 + 2 * c3 + 7 * c4 + 6 * c5 + 5 * c6 + 4 * c7 + 3 * c8 + 2 * c9 + c10
    return 1 if res % 11 == 0 else 0


print(cprnummer())
