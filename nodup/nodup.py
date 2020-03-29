import sys

def nodup(lines):
    words = lines[0].split(" ")
    if len(words) == len(set(words)):
        return "yes"

    return "no"

def main():
    lines = [line.strip() for line in sys.stdin]
    print(nodup(lines))
main()
