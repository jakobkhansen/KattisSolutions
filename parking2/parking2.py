import sys

def parking2(lines):
    numCases = int(lines[0])

    index = 1
    retStr = []
    for i in range(numCases):
        numStores = int(lines[index])
        index += 1
        stores = [int(x) for x in lines[index].split(" ")]
        retStr.append(str((max(stores)-min(stores))*2))
        index += 1
    return "\n".join(retStr)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(parking2(lines))
main()
