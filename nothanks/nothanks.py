import sys

def nothanks(lines):
    nums = [int(x) for x in lines[1].split()]
    nums = sorted(nums)
    sum = 0
    i = 0
    while i < len(nums):
        # print(nums[i])
        sum += nums[i]
        while i < len(nums)-1 and nums[i+1] == nums[i] + 1:
            # print("Skipping {}".format(nums[i]))
            i += 1
        i += 1
    return sum




def main():
    lines = [line.strip() for line in sys.stdin]
    print(nothanks(lines))
main()
