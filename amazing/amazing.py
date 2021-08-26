import sys

directions = {
    "left":(0,-1),
    "up":(1,0),
    "right":(0,1),
    "down":(-1,0)
}
opposites = {
    "left":"right",
    "up":"down",
    "right":"left",
    "down":"up"
}

visited = {(0,0): True}

def amazing():
    ret_val = recursive_search(None, (0,0))
    if ret_val == False:
        print('no way out', flush=True)

def recursive_search(came_from, position):
    visited[position] = True

    for direction in directions.keys():
        if directions != came_from:
            d_x, d_y = directions[direction]
            new_pos = (position[0] + d_x, position[1] + d_y)
            if visited.get(new_pos, False):
                continue

            print(direction, flush=True)
            response = sys.stdin.readline().strip()

            if response == 'solved':
                return 'solved'
            elif response == 'wrong':
                return 'wrong'
            elif response == 'ok':
                ret_val = None
                if not visited.get(new_pos, False):
                    ret_val = recursive_search(opposites[direction], new_pos)

                if ret_val == 'solved' or ret_val == 'wrong':
                    return ret_val

                print(opposites[direction], flush=True)
                response = sys.stdin.readline()
    return False

                



def main():
    amazing()

main()
