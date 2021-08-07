import sys
from bisect import insort_left
from queue import PriorityQueue

def continuousmedian(lines):
    for index in range(2, len(lines), 2):
        nums = [int(x) for x in lines[index].split()]
        left = PriorityQueue()
        right = PriorityQueue()

        last_1 = nums[0]
        last_2 = -1

        sum = nums[0]

        for i,num in enumerate(nums[1:]):
            # print("Inserting: {}".format(num))
            # print("Left: {}".format(left.queue))
            # print("Right: {}".format(right.queue))

            # Two numbers out case
            if i % 2 == 0:
                if num < last_1:
                    left.put((-num, num))
                    last_2 = last_1
                    last_1 = left.get()[1]
                else:
                    if last_2 == -1:
                        last_2 = num
                    else:
                        right.put(num)
                        last_2 = right.get()
                median = (last_1 + last_2) // 2


            else:
                if num < last_1:
                    left.put((-num, num))
                    right.put(last_2)
                elif num > last_2:
                    left.put((-last_1, last_1))
                    right.put(num)
                    last_1 = last_2
                else:
                    left.put((-last_1, last_1))
                    right.put(last_2)
                    last_1 = num
                median = last_1

            # print("Selected: {} {}".format(last_1, last_2))

            # print("Median found: {}".format(median))
            # print()
            sum += median
        print(sum)



            



def main():
    lines = [line.strip() for line in sys.stdin]
    continuousmedian(lines)
main()
