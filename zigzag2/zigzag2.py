import sys

increasing=True
decreasing=False
def zigzag2(lines):
    array = [int(x) for x in lines[1:]]
    largest = 0
    for i in range(len(array)):
        current = find_longest_zigzag(i, array)
        largest = current if current > largest else largest
    return largest

def find_longest_zigzag(i, array):
    if i >= len(array) - 1:
        return 1
    counter = 1
    zigzags = []

    zigzags
    for j in range(i+1, len(array)):
        if array[j] > last == rotation:
            last = array[j]
            counter += 1
            rotation = not rotation
        elif array[j] < last == rotation:
            last = array[j]
            counter += 1
            rotation = not rotation
    print("\n")
    return counter

def main():
    lines = [line.strip() for line in sys.stdin]
    print(zigzag2(lines))
main()
