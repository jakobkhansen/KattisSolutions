import sys

def heimavinna(lines):
    parts = lines[0].split(";")

    result = 0
    for part in parts:
        if "-" not in part:
            result += 1
        else:
            partRange = part.split("-")
            start = int(partRange[0])
            end = int(partRange[1])

            result += end - (start - 1)
    return result



def main():
    lines = [line.strip() for line in sys.stdin]
    print(heimavinna(lines))
main()
