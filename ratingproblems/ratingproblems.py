import sys

def ratingproblems(lines):
    n,k = [int(x) for x in lines[0].split()]
    votes_left = n - k
    votes = []
    for vote in lines[1:]:
        votes.append(int(vote))
    min_votes = votes.copy()
    max_votes = votes.copy()

    for _ in range(votes_left):
        min_votes.append(-3)
        max_votes.append(3)

    min_avg = sum(min_votes) / n
    max_avg = sum(max_votes) / n

    return f"{min_avg} {max_avg}"



def main():
    lines = [line.strip() for line in sys.stdin]
    print(ratingproblems(lines))
main()
