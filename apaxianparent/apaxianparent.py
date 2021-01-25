import sys

def apaxianparent(lines):
    Y = lines[0].split(" ")[0]
    P = lines[0].split(" ")[1]


    if Y[-1] == "e":
        return Y + "x" + P
    elif Y[-1] in ["a", "i", "o", "u"]:
        return Y[:-1] + "ex" + P
    elif Y[-2:] == "ex":
        return Y + P
    else:
        return Y + "ex" + P


def main():
    lines = [line.strip() for line in sys.stdin]
    print(apaxianparent(lines))
main()
