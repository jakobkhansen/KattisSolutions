import sys

def kemija08(lines):
    vowels = {
        'a': True,
        'e': True,
        'i': True,
        'o': True,
        'u': True
    }

    string = lines[0]
    newString = ""

    i = 0
    while i < len(string):
        newString += string[i]
        if vowels.get(string[i], False):
            i += 2
        i += 1

    return newString




def main():
    lines = [line.strip() for line in sys.stdin]
    print(kemija08(lines))
main()
