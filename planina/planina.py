import sys

def planina(lines):
    numIterations = int(lines[0].split(" ")[0])
    start = 2
    for i in range(numIterations):
        start += start - 1
    return str(start*start)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(planina(lines))
main()
