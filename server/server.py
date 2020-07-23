import sys

def server(lines):
    t = int(lines[0].split()[1])
    nums = [int(x) for x in lines[1].split()]

    time_spent = 0
    task_count = 0

    for task in nums:
        time_spent += task

        if time_spent > t:
            break

        task_count += 1

    return task_count


def main():
    lines = [line.strip() for line in sys.stdin]
    print(server(lines))
main()
