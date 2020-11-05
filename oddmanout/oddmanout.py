import sys

def oddmanout(lines):
    numCases = int(lines[0])
    caseNum = 1
    index = 1

    retStr = []
    for i in range(numCases):
        numGuests = int(lines[index])
        index += 1
        guests = [int(x) for x in lines[index].split(" ")]
        index += 1

        pairs = {}

        for guest in guests:
            pairs[guest] = pairs.get(guest, 0) + 1

        for pair in pairs.keys():
            if pairs[pair] == 1:
                retStr.append("Case #{}: {}".format(caseNum, pair))
        caseNum += 1
    return "\n".join(retStr)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(oddmanout(lines))
main()
