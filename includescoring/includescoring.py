import sys
import math

table = {
    1:100,
    2:75,
    3:60,
    4:50,
    5:45,
    6:40,
    7:36,
    8:32,
    9:29,
    10:26,
    11:24,
    12:22,
    13:20,
    14:18,
    15:16,
    16:15,
    17:14,
    18:13,
    19:12,
    20:11,
    21:10,
    22:9,
    23:8,
    24:7,
    25:6,
    26:5,
    27:4,
    28:3,
    29:2,
    30:1
}

class Score:
    def __init__(self, solved, time_penalty, last_time, on_site):
        self.solved = solved
        self.time_penalty = time_penalty
        self.last_time = last_time
        self.on_site = on_site

        self.score = on_site


    def __lt__(self, other):
        if self.solved == other.solved:
            if self.time_penalty == other.time_penalty:
                return self.last_time < other.last_time
            return self.time_penalty < other.time_penalty
        return self.solved > other.solved

    def __eq__(self, other):
        return self.solved == other.solved and self.time_penalty == other.time_penalty and self.last_time == other.last_time

    def __repr__(self) -> str:
        return f"Score({self.solved}, {self.time_penalty}, {self.last_time}, {self.on_site})"


def includescoring(lines):
    scores = []
    for i in range(1, len(lines)):
        line = lines[i]
        nums = [int(x) for x in line.split()]
        scores.append(Score(*nums))

    valid_scores = []
    for score in scores:
        valid_scores.append(score)
    valid_scores = sorted(valid_scores)


    i = 0

    while i < len(valid_scores):
        current = valid_scores[i]
        current_index = i
        equal_scores = [valid_scores[i]]
        i += 1
        while i < len(valid_scores) and valid_scores[i] == current:
            equal_scores.append(valid_scores[i])
            i += 1

        rank_sum = [table.get(j+1,0) for j in range(current_index, i)]
        # print(rank_sum)
        # print(len(rank_sum))
        # print(current_index, i)
        rank_score = math.ceil(sum(rank_sum) / len(equal_scores))
        for score in equal_scores:
            score.score += rank_score

    print("\n".join([str(x.score) for x in scores]))




def main():
    lines = [line.strip() for line in sys.stdin]
    includescoring(lines)
main()
