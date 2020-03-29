import sys

def transitwoes(lines):
    leave_time = int(lines[0].split(" ")[0])
    class_time = int(lines[0].split(" ")[1])
    num_buses = int(lines[0].split(" ")[2])

    transfer_times = [int(time) for time in lines[1].split(" ")]

    bus_times = [int(time) for time in lines[2].split(" ")]

    interval_times = [int (time) for time in lines[3].split(" ")]


    current_time = leave_time
    i = 0

    while (i < num_buses):
        current_time += bus_times[i]

        if i <= num_buses:
            current_time += interval_times[i] - (current_time % interval_times[i]) 
            current_time += transfer_times[i]
        i += 1


    if current_time <= class_time:
        return "yes"

    return "no"

        
    

def main():
    lines = [line.strip() for line in sys.stdin]
    print(transitwoes(lines))
main()
