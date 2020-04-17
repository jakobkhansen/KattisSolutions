import sys
import math

def sibice(lines):
    retString = []
    nums = [int(x) for x in lines[0].split(" ")]
    hyp = math.sqrt((nums[1]**2) + (nums[2]**2))

    for line in lines[1:]:
        num = int(line.split(" ")[0])
        if num <= hyp:
            retString.append("DA")
        else:
            retString.append("NE")

    return "\n".join(retString)




def main():
    lines = [line.strip() for line in sys.stdin]
    print(sibice(lines))
main()
