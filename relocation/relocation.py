import sys

def relocation(lines):
    locations = [int(x) for x in lines[1].split()]
    for query in lines[2:]:
        nums = [int(x) for x in query.split()]

        if nums[0] == 1:
            locations[nums[1]-1] = nums[2]
        else:
            print(abs(locations[nums[1]-1] - locations[nums[2]-1]))



def main():
    lines = [line.strip() for line in sys.stdin]
    relocation(lines)
main()
