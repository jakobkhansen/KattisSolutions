import sys

def conformity(lines):
    popularity = {}

    for courses in lines[1:]:
        courses = sorted([int(x) for x in courses.split()])
        courses_string = "".join([str(x) for x in courses])
        popularity[courses_string] = popularity.get(courses_string, 0) + 1
    highest = max(popularity.values())
    return sum([x for x in popularity.values() if x == highest])


def main():
    lines = [line.strip() for line in sys.stdin]
    print(conformity(lines))
main()
