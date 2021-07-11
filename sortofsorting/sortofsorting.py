import sys
from functools import cmp_to_key

def sortofsorting(lines):
    index = 0

    retStr = []

    while int(lines[index]) != 0:
        num_chars = int(lines[index])
        chars = lines[index+1:index+num_chars+1]
        index += num_chars+1
        bubbleSort(chars)
        retStr.append("\n".join(chars))
    return "\n\n".join(retStr)

def comp_strings(first, sec):
    if first[0] == sec[0]:
        if first[1] == sec[1]:
            return True
        return first[1] < sec[1]
    return first[0] < sec[0]

def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if not comp_strings(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    lines = [line.strip() for line in sys.stdin]
    print(sortofsorting(lines))
main()
