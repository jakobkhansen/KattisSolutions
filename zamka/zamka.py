import sys

def zamka(lines):
    retString = ""
    nums = [int(x[0]) for x in [x.split(" ") for x in lines]]
    l = nums[0]
    d = nums[1]
    x = nums[2]

    for i in range(l, d + 1):
        sum = 0
        string = str(i)
        for num in string:
            sum += int(num)

        if sum == x:
            retString += str(i) + "\n"
            break

    for i in reversed(range(l, d + 1)):
        sum = 0
        string = str(i)
        for num in string:
            sum += int(num)

        if sum == x:
            retString += str(i)
            break



    return retString



def main():
    lines = [line.strip() for line in sys.stdin]
    print(zamka(lines))
main()
