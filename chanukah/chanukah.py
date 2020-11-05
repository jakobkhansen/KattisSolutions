import sys

def chanukah(lines):
    retStr = ""
    for i,line in enumerate(lines[1:]):
        num = [int(x) for x in line.split(" ")][1]

        retStr += str(i+1) + " " + str(sum(range(num+1)) + num) + "\n"

    return retStr.strip()

def main():
    lines = [line.strip() for line in sys.stdin]
    print(chanukah(lines))
main()
