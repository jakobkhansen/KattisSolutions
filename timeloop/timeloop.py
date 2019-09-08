import sys

def timeloop(lines):
    return "".join([str(x)+" Abracadabra\n" for x in range(1, int(lines[0])+1)]).strip()

def main():
    lines = [line.strip() for line in sys.stdin]
    print(timeloop(lines))
main()
