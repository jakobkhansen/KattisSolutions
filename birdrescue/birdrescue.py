import sys

def birdrescue(lines):
    info1 = lines[0].split(" ")
    info2 = lines[1].split(" ")

    num_friend = int(info1[0])
    num_calls = int(info2[0])

    polly_pos = [int(info2[0]), int(info2[1])]
    lines = lines[2:]

    friends = []
    for friend in lines[:num_friend]:
        friend_pos = [int(x) for x in friend.split(" ")]
        pos_array = [(friend_pos[0], friend_pos[2]), (friend_pos[1], friend_pos[3])]

    lines = lines[num_friend:]
    print(lines)

    calls = [int(x) for x in lines]



def call_in_range(position, call, friend):
    # :thinking:
    pass

def main():
    lines = [line.strip() for line in sys.stdin]
    print(birdrescue(lines))
main()
