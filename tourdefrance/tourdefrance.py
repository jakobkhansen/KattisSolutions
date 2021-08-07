import sys

def tourdefrance(lines):
    curr_index = 0
    while lines[curr_index] != "0":
        f,r = [int(x) for x in lines[curr_index].split()]
        front = [int(x) for x in lines[curr_index+1].split()]
        rear = [int(x) for x in lines[curr_index+2].split()]

        drive_ratios = []

        for i in range(len(front)):
            f_s = front[i]
            for j in range(0, len(rear)):
                r_s = rear[j]
                drive_ratios.append(r_s/f_s)
        drive_ratios.sort()

        # print(len(drive_ratios))
        spreads = []
        for i in range(1, len(drive_ratios)):
            # print(i)
            diff = drive_ratios[i] / drive_ratios[i-1]
            spreads.append(diff)
        # print(spreads)



        print("{:.2f}".format(max(spreads)))





        curr_index += 3


def main():
    lines = [line.strip() for line in sys.stdin]
    tourdefrance(lines)
main()
