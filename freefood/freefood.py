import sys

def freefood(lines):
    days = {}
    for line in lines[1:]:
        num1 = int(line.split(" ")[0])
        num2 = int(line.split(" ")[1])

        for i in range(num1, num2 + 1):
            days[i] = 1

    return len(days.keys())



def main():
    lines = [line.strip() for line in sys.stdin]
    print(freefood(lines))
main()
