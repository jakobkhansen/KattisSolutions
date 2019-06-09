import sys
import math


def findColors(lines):
    num_paintings = int(lines[0])
    lines = lines[1:]

    result_list = []

    for painting_num in range(num_paintings):
        drop_list = create_drop_list(lines)
        lines = lines[int(lines[0])+1:]

        num_querys = int(lines[0])
        lines = lines[1:]

        for num_query in range(num_querys):
            query = lines[num_query].split(" ")
            x = float(query[0])
            y = float(query[1])
            result_list.append(find_color(drop_list, x, y))
        lines = lines[num_querys:]

    return "\n".join(result_list)

def create_drop_list(lines):

    num_drops = int(lines[0])
    lines = lines[1:]

    drop_list = []

    for drops in range(num_drops):
        drop = lines[drops].split(" ")

        x = float(drop[0])
        y = float(drop[1])
        v = float(drop[2])
        color = drop[3]
        radius = find_radius(v)


        drop_list.append([x, y, round(radius, 3), color])
    lines = lines[num_drops:]
    return drop_list

def find_color(drop_list, x, y):
    color = ""
    for drop in reversed(drop_list):
        drop_x = drop[0]
        drop_y = drop[1]
        radius = drop[2]

        distance = round(math.sqrt((drop_x - x) ** 2 + (drop_y - y) ** 2), 3)
        if radius > distance:
            color = drop[3]
            break
        color = "white"

    return color


def find_radius(volume):
    radius = math.sqrt(volume/math.pi)
    return radius



def main():
    lines = [line.strip() for line in sys.stdin]

    print(findColors(lines))
main()
