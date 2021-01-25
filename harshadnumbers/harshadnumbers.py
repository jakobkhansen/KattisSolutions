import sys

def harshadnumbers(lines):
    num = int(lines[0])
    current = num

    while True:
        total = 0
        copy = current
        while copy > 0:
            dig = copy%10
            total = total + dig
            copy = copy // 10

        if current % total == 0:
            return current

        current += 1



def main():
    lines = [line.strip() for line in sys.stdin]
    print(harshadnumbers(lines))
main()
