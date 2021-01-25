import sys

def missingnumbers(lines):
    expectedNum = 1
    nums = [int(x) for x in lines[1:]]
    output = []

    for num in nums:
        while num != expectedNum:
            output.append(str(expectedNum))
            expectedNum += 1
        expectedNum += 1

    if len(output) == 0:
        return "good job"

    return "\n".join(output)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(missingnumbers(lines))
main()
