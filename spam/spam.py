import sys

def spam(lines):
    k = int(lines[0])

    arr = [int(x) for x in lines[1]]
    arr = [-1 if x == 0 else 1 for x in arr]

    n = len(arr)

    max_sum = [arr[0]]
    max_subs = [[arr[0]]]

    curr_max = arr[0]
    for i in range(1, n):
        if arr[i] > curr_max+arr[i]:
            curr_max = arr[i]
            max_sum.append(curr_max)
            max_subs.append([arr[i]])
        else:
            curr_max = curr_max+arr[i]
            biggest_sub = max_subs[i-1].copy()
            biggest_sub.append(arr[i])
            max_subs.append(biggest_sub)
    print(max_subs)




def main():
    lines = [line.strip() for line in sys.stdin]
    print(spam(lines))
main()
