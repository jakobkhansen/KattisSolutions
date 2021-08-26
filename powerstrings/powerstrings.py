import sys

def powerstrings():
    for case in sys.stdin:
        if case[0] == '.':
            return

        case = case.strip()

        length = len(case)

        divisors = []
        maxi = int((length**(0.5)+1))
        for i in range(1, maxi+1):
            if length % i == 0:
                divisors.append(i)
                divisors.append(length//i)
        divisors = sorted(list(set(divisors)))


        for currentSize in divisors:
            string = case[:currentSize]*(length//currentSize)
            if string == case:
                print(length//currentSize)
                break


def main():
    powerstrings()
main()
