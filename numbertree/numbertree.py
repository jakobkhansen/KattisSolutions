import sys

def numbertree(lines):
    if len(lines[0].split()) == 1:
        height = lines[0].split()[0]
        command = ""
    else:
        height, command = lines[0].split()
    height = int(height)
    node_height = len(command)
    nodes_in_height = 2**node_height
    nodes_below = 0
    for i in range(height - node_height):
        nodes_below += 2**(height-i)

    low = nodes_below
    high = nodes_below + nodes_in_height
    # print(low, high)
    return bin_search_nums(low, high, command)

def bin_search_nums(low, high, command):
    current = (low+high)//2
    for comm in command:
        if comm == 'L':
            low = current
            current = (high+low)//2
        else:
            high = current
            current = (high+low)//2
    return current+1



def main():
    lines = [line.strip() for line in sys.stdin]
    print(numbertree(lines))
main()
