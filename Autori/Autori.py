import sys

def shortened(lines):
    line = lines[0].split("-")
    line = [person[0].capitalize() for person in line]
    return "".join(line)

def main():
    lines = [line for line in sys.stdin]

    print(shortened(lines))
main()
