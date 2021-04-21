import sys

def guess():
    current = 500
    min = 0
    max = 1000

    print(current, flush=True)

    while True:
        answer = sys.stdin.readline().strip()

        if answer == "lower":
            max = current
            current = (min + max)//2
        elif answer == "higher":
            min = current
            current = (max+min+1)//2
        else:
            break

        print(current, flush=True)


def main():
    guess()
main()
