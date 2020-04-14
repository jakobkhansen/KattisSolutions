import sys

def numberfun(lines):
    retString = ""
    for line in lines[1:]:
        retString += checkPossibleFast(line) + "\n"

    return retString.strip()

def checkPossibleFast(line):

    nums = [int(x) for x in line.split(" ")]

    num1 = nums[0]
    num2 = nums[1]
    res = nums[2]

    if num1 + num2 == res:
        return "Possible"

    if num1 - num2 == res or num2 - num1 == res:
        return "Possible"

    if num1 / num2 == res or num2 / num1 == res:
        return "Possible"

    if num1 * num2 == res:
        return "Possible"

    return "Impossible"

def checkPossible(line):
    equations = []
    nums = [int(x) for x in line.split(" ")]

    num1 = nums[0]
    num2 = nums[1]
    res = nums[2]

    for i in ["+", "-", "/", "*"]:
        equations.append("{} {} {}".format(num1, i, num2))
        equations.append("{} {} {}".format(num2, i, num1))

    for equation in equations:
        if eval(equation) == res:
            return "Possible"

    return "Impossible"




def main():
    lines = [line.strip() for line in sys.stdin]
    print(numberfun(lines))
main()
