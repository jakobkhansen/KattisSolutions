import sys

def mjehuric():

    arr = [int(x) for x in sys.stdin.readline().split()]
    while arr != sorted(arr):
        for j in range(0, len(arr)-1): 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(" ".join([str(x) for x in arr]))



def main():
    mjehuric()
main()
