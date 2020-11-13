import sys

def lostlineup(lines):
    queue = [1]*int(lines[0])

    if len(lines) == 1:
        return "1"

    try:
        for person, in_front in enumerate([int(x) for x in lines[1].split(" ")]):
            queue[in_front+1] = person + 2

        return " ".join([str(x) for x in queue])
    except Exception:
        return "1"

def main():
    lines = [line.strip() for line in sys.stdin]
    print(lostlineup(lines))
main()
