import sys

def determine_time_since_winter(linjer):
    thisYear = int(linjer[0].split(" ")[1])

    pastYears = [int(tall) for tall in linjer[1].split(" ")]

    calced = calc_years(thisYear, pastYears)

    if calced != -1:
        return "It hadn't snowed this early in " + str(calced) + " years!"
    else:
        return "It had never snowed this early!"

def calc_years(thisYear, pastYears):
    counter = 0

    for year in pastYears:
        if year <= thisYear:
            break
        else:
            counter += 1


    if counter == len(pastYears):
        counter = -1
    return counter

def main():
    linjer = [linje.strip() for linje in sys.stdin]
    print(determine_time_since_winter(linjer))
main()
