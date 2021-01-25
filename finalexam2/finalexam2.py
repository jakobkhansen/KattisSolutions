import sys

def finalexam2(lines):
    score = 0
    for i in range(1, len(lines)):
        if lines[i] == lines[i-1]:
            score += 1
    return score



def main():
    lines = [line.strip() for line in sys.stdin]
    print(finalexam2(lines))
main()
