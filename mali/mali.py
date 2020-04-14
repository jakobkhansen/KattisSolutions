import sys

def mali(lines):
    min_a = -1
    min_b = -1

    max_a = 0
    max_b = 0

    
    retString = ""

    for line in lines[1:]:
        nums = [int(x) for x in line.split(" ")]

        min_a = nums[0] if (min_a == -1) or nums[0] < min_a else min_a
        min_b = nums[1] if (min_b == -1) or nums[1] < min_b else min_b

        max_a = nums[0] if max_a < nums[0] else max_a
        max_b = nums[1] if max_b < nums[1] else max_b

        retString += findMinCombo(min_a, min_b, max_a, max_b) + "\n"

    return retString.strip()



def findMinCombo(min_a, min_b, max_a, max_b):
    pot1 = min_a + max_b
    pot2 = min_b + max_a

    return str(pot1) if pot1 > pot2 else str(pot2)

def main():
    lines = [line.strip() for line in sys.stdin]
    print(mali(lines))
main()
