import sys

def isithalloween(lines):
    if lines[0] == "OCT 31" or lines[0] == "DEC 25":
        return "yup"

    return "nope"


def main():
    lines = [line.strip() for line in sys.stdin]
    print(isithalloween(lines))
main()
