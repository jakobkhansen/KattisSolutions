import sys

def grading():
    gradings = [int(x) for x in input().split()]
    letters = ['A', 'B', 'C', 'D', 'E']
    score = int(input())
    for i,grade in enumerate(gradings):
        if score >= grade:
            return letters[i]

    return 'F'


def main():
    print(grading())
main()
