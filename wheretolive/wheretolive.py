import sys

def wheretolive(lines):
    curr_index = 0
    while lines[curr_index] != "0":
        n = int(lines[curr_index])
        important_places = []
        for line in lines[curr_index+1:curr_index+n+1]:
            x,y = [int(x) for x in line.split()]
            important_places.append((x,y))


        best_distance = sys.maxsize
        best_point = 0,0

        for i in range(1000):
            for j in range(1000):
                distances = []
                for point in important_places:
                    distances.append(straight_distance((i,j), point))
                average = sum(distances) / len(distances)
                if average < best_distance:
                    best_distance = average
                    best_point = (i,j)
                if i == 51 and j == 32:
                    print(average)
        print(best_distance)

        curr_index += n+1

def straight_distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(wheretolive(lines))
main()
