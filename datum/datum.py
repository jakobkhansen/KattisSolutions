import sys
import datetime

def datum(lines):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = int(lines[0].split(" ")[0])
    month = int(lines[0].split(" ")[1])

    date = datetime.datetime(2009, month, day)

    return days[date.weekday()]


def main():
    lines = [line.strip() for line in sys.stdin]
    print(datum(lines))
main()
