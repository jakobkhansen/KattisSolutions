import sys

def speedlimit(lines):
    ret = ""
    while (lines[0] != "-1"):
        num_measures = int(lines[0])
        num_total = 0
        num_previous = 0
        for m in range(1, num_measures + 1):
            measure = lines[m].split(" ")
            speed = int(measure[0])

            num_hours = int(measure[1]) - num_previous
            num_total += num_hours * speed 
            num_previous = int(measure[1])

        ret += "{} miles\n".format(num_total)
        lines = lines[num_measures + 1:]
    return ret.strip()
            


def main():
    lines = [line.strip() for line in sys.stdin]
    print(speedlimit(lines))
main()
