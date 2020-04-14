import sys

def avion(lines):
    retString = ""
    for i, line in enumerate(lines):
        if "FBI" in line:
            retString += str(i+1) + " "

    if retString == "":
        return "HE GOT AWAY!"

    return retString.strip()


def main():
    lines = [line.strip() for line in sys.stdin]
    print(avion(lines))
main()
