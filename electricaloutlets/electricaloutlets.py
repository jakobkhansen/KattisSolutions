import sys

def electricaloutlets(lines):
    numCases = int(lines[0])
    ret = []
    for i in range(1, numCases+1):
        case = [int(x) for x in lines[i].split(" ")]
        ret.append(str(sum(map(lambda x: x-1, case[1:]))+1))
    return "\n".join(ret)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(electricaloutlets(lines))
main()
