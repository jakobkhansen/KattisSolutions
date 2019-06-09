import sys


def findCombos(linjer):
    numColumns = int(linjer[0].split(" ")[1])
    piece = int(linjer[0].split(" ")[0])
    brett = []
    for i in range(5):
        brett.append([])

    colored = linjer[1]

    for kolonne in range(len(brett)):
        for rad in colored.split(" "):
            if int(rad) > kolonne:
                brett[len(brett) - kolonne - 1].append("*")
            else:
                brett[len(brett) - kolonne - 1].append("0")

    string = ""

    for rad in brett:
        for char in rad:
            string += char
        string += "\n"
    print(string)



def main():
    linjer = [linje for linje in sys.stdin]

    print(findCombos(linjer))
main()
