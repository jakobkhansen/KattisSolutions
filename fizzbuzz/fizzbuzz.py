import sys

def fizzbuzz(lines):
    nums = lines[0].split(" ")
    x = int(nums[0])
    y = int(nums[1])
    n = int(nums[2])

    values = {
        x: "Fizz",
        y: "Buzz"
    }

    ret = []
    for i in range(1, n+1):

        streng = ""
        for j in values.keys():
            if i % j == 0:
                streng += values[j]

        if streng == "":
            streng = str(i)

        ret.append(streng)

    return "\n".join(ret)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(fizzbuzz(lines))
main()
