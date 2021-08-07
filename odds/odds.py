import sys
from fractions import Fraction

def odds(lines):
    for game in lines[:-1]:
        game = game.split()
        possible_strings = [game]

        for i in range(4):
            new_strings = []
            for curr_string in possible_strings:
                # print(curr_string)
                if curr_string[i] == '*':
                    for j in range(1,7):
                        new_str = curr_string.copy()
                        new_str[i] = str(j)
                        new_strings.append(new_str)
                else:
                    new_strings.append(curr_string)
            possible_strings = new_strings

        won = 0

        for string in possible_strings:
            a1, a2, b1, b2 = [int(x) for x in string]
            won += result(a1, a2, b1, b2)

        reduced = Fraction(won, len(possible_strings))

        print(str(reduced))


def result(a1, a2, b1, b2):
    special = {
        (1,2): 100,
        (2,1): 100,
        (6,6): 99,
        (5,5): 98,
        (4,4): 97,
        (3,3): 96,
        (2,2): 95,
        (1,1): 94,
    }
    a1,a2 = sorted([a1,a2], reverse=True)
    b1,b2 = sorted([b1,b2], reverse=True)

    p1_value = special.get((a1,a2), int(f"{a1}{a2}"))
    p2_value = special.get((b1,b2), int(f"{b1}{b2}"))

    return 1 if p1_value > p2_value else 0

def main():
    lines = [line.strip() for line in sys.stdin]
    odds(lines)
main()
