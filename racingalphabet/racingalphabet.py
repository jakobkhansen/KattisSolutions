import sys
import string
import math

def racingalphabet(lines):
    circumference = 60*math.pi
    distance_between = circumference / 28
    # print(distance_between)
    alphabet = list(string.ascii_uppercase)
    alphabet.append(" ")
    alphabet.append("'")
    pos = {alphabet[x] : x for x in range(len(alphabet))}

    for line in lines[1:]:
        curr_pos = pos[line[0]]
        length = 0
        for letter in line:
            pass
            letter_pos = pos[letter]
            # Move

            distance = min(abs(letter_pos - curr_pos), (curr_pos + letter_pos) % 28)
            # print(distance)

            length += (distance*distance_between) / 15
            length += 1

            # Place

            # print(letter)
            curr_pos = letter_pos
        print(length)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(racingalphabet(lines))
main()
