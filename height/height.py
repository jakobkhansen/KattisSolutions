import sys

def height(lines):
    n = int(lines[0])
    for case in range(n):
        array = [int(x) for x in lines[case+1].split()[1:]]
        print(f'{case+1} {insertion_sort(array)}')


def insertion_sort(arr):
    swap_count = 0
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            swap_count += 1
            arr[j],arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return swap_count

def main():
    lines = [line.strip() for line in sys.stdin]
    (height(lines))
main()
