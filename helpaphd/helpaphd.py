import sys

def helpaphd(lines):
    for add in lines[1:]:
        if add == "P=NP":
            print("skipped")
        else:
            print(eval(add))


def main():
    lines = [line.strip() for line in sys.stdin]
    helpaphd(lines)
main()
