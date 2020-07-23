import sys

def quickestimate(lines):
    retString = ""
    for num in lines[1:]:
        retString += str(len(num)) + "\n"

    return retString.strip()


def main():
    lines = [line.strip() for line in sys.stdin]
    print(quickestimate(lines))
main()
