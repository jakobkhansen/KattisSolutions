import sys

def biggerNum(lines):
    line = lines[0].split(" ")
    num1 = int("".join(reversed(line[0])))
    num2 = int("".join(reversed(line[1])))
    return max(num1, num2)

def main():
    lines = [line.strip() for line in sys.stdin]

    print(biggerNum(lines))
main()
