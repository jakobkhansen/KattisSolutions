import sys

def heartrate(lines):
    for case in lines[1:]:
        b,p = [float(x) for x in case.split(" ")]
        bpm = (60*b)/p
        dev = 60/p
        min = bpm - dev
        max = bpm + dev
        print(min, bpm, max)


def main():
    lines = [line.strip() for line in sys.stdin]
    heartrate(lines)
main()
