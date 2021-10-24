import sys

def recount(lines):
    votes = {}
    for line in lines[:-1]:
        name = line.strip()
        votes[name] = votes.get(name, 0) + 1

    votes_sorted = sorted(votes.items(), key=lambda x: x[1])
    if votes_sorted[-1][1] == votes_sorted[-2][1]:
        return "Runoff!"

    return votes_sorted[-1][0]

def main():
    lines = [line.strip() for line in sys.stdin]
    print(recount(lines))
main()
