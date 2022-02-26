import sys

def findingana():
    inp = input()
    for i,char in enumerate(inp):
        if char == 'a':
            return inp[i:]


def main():
    print(findingana())
main()
