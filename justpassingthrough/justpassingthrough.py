import sys


def justpassingthrough(lines):
    roadtrip = []

    num_passes = int(lines[0].split(" ")[2])

    for line in lines[1:]:
        roadtrip.append([int(x) for x in line.split(" ")])

    passes = identifyPasses(roadtrip)

    return findBestPath(roadtrip, passes, num_passes)

def findBestPath(roadtrip, passes, num_passes):
    lowest = findBestPathRecursive(roadtrip, passes, 0, 0, 0, 0, num_passes)
    for i in range(1, len(roadtrip)):
        potential = findBestPathRecursive(roadtrip, passes, i, 0, 0, 0, num_passes)
        if lowest == -1 or potential < lowest and potential != -1:
            lowest = potential

    if lowest == -1:
        return "impossible"

    return lowest


def findBestPathRecursive(roadtrip, passes_arr, x, y, total, passes, wanted_passes):


    if roadtrip[x][y] == -1:
        return -1

    total += roadtrip[x][y]

    if passes_arr[x][y] == 1:
        passes += 1

    if y == len(roadtrip[0]) - 1:

        if passes == wanted_passes:
            return total

        return -1


    lowest = findBestPathRecursive(roadtrip, passes_arr, x, y+1, total, passes, wanted_passes)
    

    if x > 0:
        potential_high = findBestPathRecursive(roadtrip, passes_arr, x-1, y+1, total, passes, wanted_passes)
        if lowest == -1 or potential_high < lowest and potential_high != -1:
            lowest = potential_high

    if x < len(roadtrip) - 1:
        potential_low = findBestPathRecursive(roadtrip, passes_arr, x+1, y+1, total, passes, wanted_passes)

        if lowest == -1 or potential_low < lowest and potential_low != -1:
            lowest = potential_low


    return lowest


def identifyPasses(matrix):
    passes = []
    for i, array in enumerate(matrix):

        line = []

        for j, num in enumerate(array):

            if (num == -1):
                line.append(0)

            elif i == 0 or j == 0:
                line.append(0)
            elif i == len(matrix) - 1 or j == len(array) - 1:
                line.append(0)

            elif matrix[i][j-1] < num and matrix[i][j+1] < num:
                if matrix[i-1][j] > num and matrix[i+1][j] > num:
                    line.append(1)
                else:
                    line.append(0)

            else:
                line.append(0)

        passes.append(line)

    return passes



def main():
    lines = [line.strip() for line in sys.stdin]
    print(justpassingthrough(lines))
main()
