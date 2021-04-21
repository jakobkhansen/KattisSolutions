import sys

def trainboarding(lines):
    n,l,p = [int(x) for x in lines[0].split(" ")]
    trains = [0]*n
    max_distance = 0
    for num_str in lines[1:]:
        num = int(num_str)
        distance, index = get_train_index_and_distance(num, l, n)
        max_distance = distance if distance > max_distance else max_distance
        trains[index] += 1
    print(max_distance)
    print(max(trains))


def get_train_index_and_distance(pos, length, num_cars):
    if pos >= length*num_cars:
        index = num_cars-1
    else:
        index = int(pos/length)
    door_pos = (index*length) + length/2
    distance = int(abs(pos - door_pos))
    return distance, index

def main():
    lines = [line.strip() for line in sys.stdin]
    (trainboarding(lines))
main()
