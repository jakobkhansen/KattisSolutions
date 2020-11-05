import sys
import math

def lastfactorialdigit(lines):
    retStr = ""
    for i in lines[1:]:
        num = int(i)
        retStr += str(math.factorial(num))[-1] + "\n"
    return retStr.strip()


def main():
    lines = [line.strip() for line in sys.stdin]
    print(lastfactorialdigit(lines))
main()
