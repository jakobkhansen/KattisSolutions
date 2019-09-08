import sys

def sibice(lines):
    w = int(lines[0].split(" ")[1])
    h = int(lines[0].split(" ")[2])

    streng = []
    for line in lines[1:]:
        if int(line) <= w or int(line) <= h:
            streng.append("DA")
        else:
            streng.append("NE")

    return "\n".join(streng)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(sibice(lines))
main()
