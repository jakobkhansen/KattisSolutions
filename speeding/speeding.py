import sys

def speeding(lines):
    checkpoints = lines[1:]
    checkpoints = [(int(x.split()[0]), int(x.split()[1])) for x in checkpoints]
    speeds = []

    for i,(time, distance) in enumerate(checkpoints[1:]):
        prev_time, prev_speed = checkpoints[i]
        time_diff = time - prev_time
        distance_diff = distance - prev_speed
        speed = int(distance_diff / time_diff)
        speeds.append(speed)
    return max(speeds)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(speeding(lines))
main()
