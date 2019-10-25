import sys
import math

def shuffling(lines):
    line = lines[0].split(" ")

    num = int(line[0])
    shuffle_type = line[1]

    original = []

    for i in range(1, num+1):
        original.append(i)

    new_deck = original.copy()
    # print(new_deck)
    counter = 1

    methodPicker = {
        "out":out_shuffle,
        "in":in_shuffle
    }

    function = methodPicker[shuffle_type]

    new_deck = function(new_deck)
    while (new_deck != original):
        counter += 1
        new_deck = function(new_deck)
        # print(new_deck, end="")
        # print(original)


    # print(new_deck)
    return counter




def out_shuffle(deck):
    left_size = math.ceil(len(deck) / 2)
    right_size = len(deck) // 2
    left_deck = deck[:left_size]

    if (left_size != right_size):
        right_deck = deck[right_size+1:]
    else:
        right_deck = deck[right_size:]

    # print(left_deck, end="")
    # print(right_deck)

    new_deck = []


    while (len(left_deck) > 0 or len(right_deck) > 0):

        if (len(left_deck) > 0):
            new_deck.append(left_deck.pop(0))

        if (len(right_deck) > 0):
            new_deck.append(right_deck.pop(0))

    return new_deck

def in_shuffle(deck):
    left_size = len(deck) // 2
    right_size = math.ceil(len(deck) / 2)


    left_deck = deck[:left_size]

    if (left_size != right_size):
        right_deck = deck[right_size-1:]
    else:
        right_deck = deck[right_size:]


    new_deck = []

    while (len(left_deck) > 0 or len(right_deck) > 0):

        if (len(right_deck) > 0):
            new_deck.append(right_deck.pop(0))

        if (len(left_deck) > 0):
            new_deck.append(left_deck.pop(0))


    return new_deck




def main():
    lines = [line.strip() for line in sys.stdin]
    print(shuffling(lines))
main()
