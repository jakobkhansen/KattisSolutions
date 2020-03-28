import sys

def eatingout(lines):
    nums = [int(num) for num in lines[0].split(" ")]
    m = nums[0]
    a = nums[1]
    b = nums[2]
    c = nums[3]

    arr = [0]*m
    arr_index = 0

    for num in nums[1:]:
        arr[0:num] = [1]

    print(arr)







def main():
    lines = [line.strip() for line in sys.stdin]
    print(eatingout(lines))
main()
