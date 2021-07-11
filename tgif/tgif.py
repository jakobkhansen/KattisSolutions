import sys

DAYS = {
    "MON":1,
    "TUE":2,
    "WED":3,
    "THU":4,
    "FRI":5,
    "SAT":6,
    "SUN":7
}

MONTHS = [
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC"
]

MONTH_LENGTH = {
    "JAN": 31,
    "FEB": 28,
    "MAR": 31,
    "APR": 30,
    "MAY": 31,
    "JUN": 30,
    "JUL": 31,
    "AUG": 31,
    "SEP": 30,
    "OCT": 31,
    "NOV": 30, 
    "DEC": 31
}

def tgif(lines):
    curr_day, curr_month = lines[0].split()
    curr_day = int(curr_day)
    days_since = 0
    for month in MONTHS:
        if month == curr_month:
            break
        days_since += MONTH_LENGTH[month]
    days_since += curr_day-1
    day_of_week_start = DAYS[lines[1]]
    day_of_week = (day_of_week_start + days_since) % 7

    if (day_of_week == 5 or day_of_week == 4) and MONTHS.index(curr_month) > 1:
        return "not sure"

    if day_of_week == 5:
        return "TGIF"

    return ":("




def main():
    lines = [line.strip() for line in sys.stdin]
    print(tgif(lines))
main()
