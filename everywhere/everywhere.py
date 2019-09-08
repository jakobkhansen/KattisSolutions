import sys

def everywhere(lines):
    num_cases = int(lines[0])
    lines = lines[1:]

    streng = []
    for i in range(num_cases):
        cities = lines[1:int(lines[0])+1]

        num_cities = len(list(set(cities)))
        streng.append(str(num_cities))

        lines = lines[int(lines[0])+1:]

    return "\n".join(streng)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(everywhere(lines))
main()
