import sys

def wheresmyinternet(lines):
    connected = {}
    for line in lines:
        for num in line.split(" "):
            connected[int(num)] = False
    connected[1] = True
    print(connected)

    for num in connected.keys():

        num = int(num)
        isConnected(num, lines, connected)

    print(connected)

def isConnected(num, lines, connected):
    if connected[num]:
        return True

    for line in lines:
        print(num)
        num1 = int(line.split(" ")[0])
        num2 = int(line.split(" ")[1])

        if (num1 == num and isConnected(num2, lines, connected)):

            connected[num] = True
            return True

        if (num2 == num and isConnected(num1, lines, connected)):

            connected[num] = True
            return True

    return False


def main():
    lines = [line.strip() for line in sys.stdin]
    print(wheresmyinternet(lines))
main()
