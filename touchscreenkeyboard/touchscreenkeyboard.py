import sys

def touchscreenkeyboard():
    # This is silly, but I did it in Vim soooo

    cases = int(input())

    for _ in range(cases):
        word, n = input().split()
        n = int(n)
        candidates = [input() for _ in range(n)]
        diffs = sorted([[compare(word, x), x] for x in candidates], key=lambda x : x[1])
        diffs = sorted(diffs, key=lambda x : x[0])

        print("\n".join([" ".join([x[1], str(x[0])]) for x in diffs]))

def compare(word, candidate):
    table = {
        'q': (0,0),
		'w': (0,1),
		'e': (0,2),
		'r': (0,3),
		't': (0,4),
		'y': (0,5),
		'u': (0,6),
		'i': (0,7),
		'o': (0,8),
		'p': (0,9),

		'a': (1,0),
		's': (1,1),
		'd': (1,2),
		'f': (1,3),
		'g': (1,4),
		'h': (1,5),
		'j': (1,6),
		'k': (1,7),
		'l': (1,8),

		'z': (2,0),
		'x': (2,1),
		'c': (2,2),
		'v': (2,3),
		'b': (2,4),
		'n': (2,5),
		'm': (2,6),
    }
    diff = 0
    for w_char, c_char in zip(word, candidate):
        word_pos = table[w_char]
        cand_pos = table[c_char]
        diff += abs(word_pos[0] - cand_pos[0])
        diff += abs(word_pos[1] - cand_pos[1])
    return diff


touchscreenkeyboard()
