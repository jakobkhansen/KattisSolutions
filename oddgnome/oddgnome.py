import sys

def oddgnome(lines):
    n = int(lines[0])

    for line in lines[1:]:
        gnomes = [int(x) for x in line.split(" ")]

        for i in range(2, len(gnomes)-1):
            if gnomes[i] != (gnomes[i-1] + 1):
                print(i)
                break


def main():
    lines = [line.strip() for line in sys.stdin]
    oddgnome(lines)
main()
