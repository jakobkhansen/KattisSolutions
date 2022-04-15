import sys
import math

def pyramids():
    blocks = int(input())
    curr_layer = 1

    while curr_layer**2 <= blocks:
        blocks -= curr_layer**2
        curr_layer += 2

    return (curr_layer-1) // 2



def main():
    print(pyramids())
main()
