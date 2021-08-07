import sys

def magictrick(lines):
    word_dict = {}
    for char in lines[0]:
        old_val = 0 if not word_dict.get(char) else word_dict[char]
        word_dict[char] = old_val + 1
    max_occ = max(word_dict, key=word_dict.get)
    return 1 if word_dict[max_occ] == 1 else 0


def main():
    lines = [line.strip() for line in sys.stdin]
    print(magictrick(lines))
main()
