import sys

def fyi(lines):
    return 1 if lines[0][:3] == "555" else 0


def main():
    lines = [line.strip() for line in sys.stdin]
    print(fyi(lines))
main()
