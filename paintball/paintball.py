import sys

def paintball(lines):
    numPlayers = int(lines[0].split(" ")[0])
    shootable_by = [[] for _ in range(numPlayers + 1)]


    for line in lines[1:]:
        nums = [int(x) for x in line.split(" ")]
        shootable_by[nums[0]].append(nums[1])
        shootable_by[nums[1]].append(nums[0])

    print(shootable_by)
    fired = [0]*(numPlayers + 1)

    for shooters in shootable_by[1:]:
        if shooters == []:
            return "Impossible"



def main():
    lines = [line.strip() for line in sys.stdin]
    print(paintball(lines))
main()
