import sys

def findQaly(lines):
    lines = lines[1:]

    qaly_sum = 0
    for line in lines:
        numbers = line.split(" ")

        quality = float(numbers[0])

        period = float(numbers[1])

        qaly = quality*period

        qaly_sum += qaly
    return qaly_sum


def main():
    lines = [line for line in sys.stdin]

    print(findQaly(lines))
main()
