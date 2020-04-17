import sys

def exam(lines):
    my_answers = lines[1]
    friends_answers = lines[2]
    numQ = len(lines[1])
    friend_correct = int(lines[0].split(" ")[0])
    friend_wrong = numQ - friend_correct


    my_score = 0
    for i in range(numQ):
        if my_answers[i] == friends_answers[i]:
            if friend_correct > 0:
                my_score += 1
                friend_correct -= 1
        
        else:
            if friend_wrong > 0:
                my_score += 1
                friend_wrong -= 1
    return str(my_score)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(exam(lines))
main()
