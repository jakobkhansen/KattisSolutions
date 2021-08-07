import sys

def throwns(lines):
    n,k = [int(x) for x in lines[0].split()]
    locations = [0]*100
    location_index = 0

    commands = lines[1].split()
    command_index = 0
    while command_index < len(commands):
        if commands[command_index] == "undo":
            undo_amount = int(commands[command_index+1])
            location_index -= undo_amount
            command_index += 2
        else:
            throw_len = int(commands[command_index])
            old_location = locations[location_index]
            location_index += 1
            locations[location_index] = (old_location + throw_len) % n
            command_index += 1
    return locations[location_index]



def main():
    lines = [line.strip() for line in sys.stdin]
    print(throwns(lines))
main()
