import sys

def cups(lines):
    values = []

    for color_line in lines[1:]:
        line_split = color_line.split(" ")

        if line_split[0].isnumeric():
            values.append([int(line_split[0])/2, line_split[1]])
        elif line_split[1].isnumeric():
            values.append([int(line_split[1]), line_split[0]])
    values.sort(key=lambda x: x[0])

    return "\n".join(map(lambda x: x[1], values))



def main():
    lines = [line.strip() for line in sys.stdin]
    print(cups(lines))
main()
