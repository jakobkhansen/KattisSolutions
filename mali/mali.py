import sys
def countingSort(array, maxValue):
    count_arr = [0]*maxValue

    for i in array:
        count_arr[i] += 1

    index = 0
    for i in range(len(count_arr)):
        for _ in range(count_arr[i]):
            array[index] = i
            index += 1


def mali(lines):
    left = []
    right = []
    for a,b in [map(int, x.split()) for x in lines[1:]]:
        left.append(a)
        right.append(b)

        countingSort(left, 100)
        countingSort(right, 100)

        largestMinPair = 0

        j = 0
        k = len(left) - 1

        while (k >= 0):
            print("Candidate: {} {}".format(left[j], right[k]))
            candidate = left[j] + right[k]
            print(candidate)
            if candidate > largestMinPair:
                largestMinPair = candidate
            j += 1
            k -= 1

        print(largestMinPair)




def main():
    lines = [line.strip() for line in sys.stdin]
    mali(lines)
main()
