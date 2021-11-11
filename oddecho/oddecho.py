import sys

def oddecho(lines):
    for i in range(1, len(lines), 2):
        print(lines[i])



def main():
    lines = [line.strip() for line in sys.stdin]
    oddecho(lines)
main()
