import sys

def ptice(lines):
    adrian = ['A', 'B', 'C']

    bruno = ['B', 'A', 'B', 'C']

    goran = ['C', 'C', 'A', 'A', 'B', 'B']

    scores = [0, 0, 0]

    sequence = lines[1]

    for i, answer in enumerate(sequence):
        for j, person in enumerate([adrian, bruno, goran]):
            p_answer = person[i % len(person)]
            scores[j] += 1 if p_answer == answer else 0

    people = [["Adrian", scores[0]], ["Bruno", scores[1]], ["Goran", scores[2]]]

    max_score = max(people, key=lambda x: x[1])
    print(max_score[1])
    for person in people:
        if person[1] == max_score[1]:
            print(person[0])




def main():
    lines = [line.strip() for line in sys.stdin]
    ptice(lines)
main()
