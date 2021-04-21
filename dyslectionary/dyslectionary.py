import sys

class Word:
    def __init__(self, word):
        self.word = word
        self.reverse = word[::-1]

    def __lt__(self, other):
        return self.reverse < other.reverse

    def __repr__(self):
        return self.word

def dyslectionary(lines):
    groups = []
    index = 0
    curr_group = []
    for line in lines:
        if line == "":
            groups.append(curr_group)
            curr_group = []
        else:
            curr_group.append(line.strip())
    groups.append(curr_group)

    for i, group in enumerate(groups):
        words = []
        for word in group:
            words.append(Word(word))
        words.sort()
        padding = len(max(group, key=lambda x: len(x)))

        for word in words:
            pad = padding - len(word.word)
            print((' '*pad) + word.word)

        if i != len(groups)-1:
            print()



def main():
    lines = [line.strip() for line in sys.stdin]
    (dyslectionary(lines))
main()
