import sys


def froggie(lines):
    directions = {
        'U':[-1,0],
        'D':[1,0],
        'L':[0,-1],
        'R':[0,1]
    }
    l,w = [int(x) for x in lines[0].split()]
    road = [['.' for y in range(w)] for x in range(l+1)]
    offsets = [int(x.split()[0]) for x in lines[1:l+1]]
    intervals = [int(x.split()[1]) for x in lines[1:l+1]]
    speeds = [int(x.split()[2]) for x in lines[1:l+1]]

    froggie = [l,int(lines[-1].split()[0])]


    commands = [x for x in lines[-1].split()[1]]

    time = 0


    for command in commands:
        dir = directions[command]
        update(road,speeds,intervals,offsets,time)
        # print_road(road,froggie)
        froggie = [froggie[0]+dir[0],froggie[1]+dir[1]]
        # print()

        # print("froggie",froggie)
        safe = get_safe_squares(road,speeds,intervals,offsets,time)

        if froggie[0] < 0:
            return "safe"


        if in_range(froggie,l,w):
            # print("in range")
            if not safe[froggie[0]][froggie[1]]:
                # print("squish by car")
                return "squish"

        time += 1


    # print("squish by command")
    return "squish"

def in_range(froggie,l,w): 
    x,y = froggie
    return x >= 0 and y >= 0 and x < l and y < w;

def check_jumped_into_car(road,froggie,command):
    road_direction = 1 if froggie[0] % 2 == 0 else -1
    if road[froggie[0]][froggie[1]] == 'c':

        # Frog on right
        if road_direction == 1 and command == 'L':
            return True

        # Frog on right
        if road_direction == -1 and command == 'R':
            return True
    return False


def update(road, speeds, intervals, offsets,time):
    for i in range(len(road)):
        for j in range(len(road[i])):
            road[i][j] = '.'

    direction = 1
    for i in range(len(road)-1):
        row =road[i]
        for j,cell in enumerate(row):
            if direction == -1:
                new_offset = (((len(row)-1) % intervals[i])+(offsets[i]+(speeds[i]*time))%intervals[i]) %intervals[i]
            else:
                new_offset = ((offsets[i]+(speeds[i]*time)) % intervals[i])

            if j % intervals[i] == 0 and 0 <= j+new_offset < len(row):
                row[j+new_offset] = 'c'
        direction *= -1

def get_safe_squares(road, speeds, intervals, offsets,time):
    safe = [[True for _ in x] for x in road]
    direction = 1
    for i in range(len(road)-1):
        row = road[i]
        if speeds[i] == 0:
            for j,cell in enumerate(row):
                if direction == -1:
                    # print(i,j)
                    # print("interval={}".format(intervals[i]))
                    # print("left={}".format((len(row)-1 - j) % intervals[i]))
                    # print("right={}".format(((len(row)-1) - offsets[i]) % intervals[i]))
                    if (len(row)-1 - j) % intervals[i] == offsets[i]:
                        # print(i,j)
                        safe[i][j] = False
                else:
                    if j % intervals[i] == offsets[i]:
                        safe[i][j] = False
            direction *= -1
            continue

        for j in range(-intervals[i], len(row)+intervals[i]):
            if direction == -1:
                new_offset = (((len(row)-1) % intervals[i])+(offsets[i]+(speeds[i]*time))%intervals[i]) %intervals[i]
            else:
                new_offset = ((offsets[i]+(speeds[i]*time)) % intervals[i])

            for k in range(1*direction,(speeds[i]*direction)+1*direction,direction):
                if (j % intervals[i])*direction == 0 and 0 <= j+new_offset+k < len(row):
                    safe[i][j+new_offset+k] = False
                    # print(i,j+new_offset+k, "not safe")
            # print()
        direction *= -1
    return safe







def print_road(board,froggie):
    board[froggie[0]][froggie[1]] = 'f'
    out = ""
    for row in board:
        for cell in row:
            out += cell
        out += "\n"
    print(out.strip())

def main():
    lines = [line.strip() for line in sys.stdin]
    print(froggie(lines))
main()
