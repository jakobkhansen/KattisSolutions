import sys

def bard(lines):
    n = int(lines[0])
    e = int(lines[1])

    song_dict = {x : list() for x in list(range(2, n+1))}
    next_song = 0
    for line in lines[2:]:
        nums = [int(x) for x in line.split()]
        attending = nums[1:]
        if 1 in attending:
            next_song += 1
            for villager in attending:
                if villager != 1:
                    song_dict[villager].append(next_song)
                    song_dict[villager] = list(set(song_dict[villager]))
        else:
            known_songs = []
            for x in [song_dict[y] for y in attending]:
                known_songs += x
            known_songs = list(set(known_songs))
            for x in attending:
                song_dict[x] = known_songs.copy()
    knows_all = ["1"]
    for villager in list(range(2, n+1)):
        if len(song_dict[villager]) == next_song:
            knows_all.append(str(villager))
    return "\n".join(knows_all)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(bard(lines))
main()
