import sys

def reseto(lines):
    n,k = [int(x) for x in lines[0].split()]
    nums = [False for i in range(n+1)]

    numsCrossed = 0

    for i in range(2,n+1):
        for j in range(i, n+1, i):
            if not nums[j]:
                nums[j] = True
                numsCrossed += 1
                if numsCrossed == k:
                    return j


def main():
    lines = [line.strip() for line in sys.stdin]
    print(reseto(lines))
main()
