import sys

def stopwatch(lines):
    lines = lines[1:]
    current = int(lines[0])
    total = 0
    mod = 1
    for line in lines[1:]:
        num = int(line)
        diff = num - current
        total += diff*mod

        current = num
        mod = (mod + 1) % 2

    if mod == 1:
        return "still running"
    return total



def main():
    lines = [line.strip() for line in sys.stdin]
    print(stopwatch(lines))
main()
