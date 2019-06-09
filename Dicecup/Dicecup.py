import sys

def highest_probability(lines):
    line = lines[0].split(" ")
    dice1 = int(line[0])
    dice2 = int(line[1])

    highest_sum = dice1 + dice2

    array_results = []

    for range1 in range(1, dice1+1):
        for range2 in range(1, dice2+1):
            array_results.append(range1 + range2)

    highest_first = max(array_results, key=array_results.count)
    most_common_list = []
    [most_common_list.append(val) for val in array_results if array_results.count(val) == array_results.count(highest_first) and val not in most_common_list]

    return "\n".join(map(str, most_common_list))

def main():
    lines = [line for line in sys.stdin]
    print(highest_probability(lines))
main()
