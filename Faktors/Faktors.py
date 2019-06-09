import sys

def find_num_bribes(lines):
    line = lines[0].split(" ")

    articles = int(line[0])
    impact_goal = int(line[1])

    return (articles * (impact_goal-1)) + 1

def main():
    lines = [line for line in sys.stdin]
    print(find_num_bribes(lines))
main()
