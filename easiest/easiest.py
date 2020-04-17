import sys

def easiest(lines):
    nums = [int(x) for x in lines[:-1]]
    retString = []
    for num in nums:
        sumofnum = sum_digits(num)

        i = 11
        while True:
            multiplied = num*i
            if sum_digits(multiplied) == sumofnum:
                retString.append(str(i))
                break
            i += 1
    return "\n".join(retString)

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10

    return s


def main():
    lines = [line.strip() for line in sys.stdin]
    print(easiest(lines))
main()
