import sys

def teacherevaluation(lines):
    num_results = int(lines[0].split(" ")[0])
    p = int(lines[0].split(" ")[1])

    results = [int(num) for num in lines[1].split(" ")]

    result_sum = sum(results)

    if p == 100:
        return "impossible"

    i = 0
    while (result_sum / num_results < p):
        result_sum += 100
        num_results += 1
        i += 1
    return i


def main():
    lines = [line.strip() for line in sys.stdin]
    print(teacherevaluation(lines))
main()
