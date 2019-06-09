import sys

def calc(linje, definisjoner):
    liste = [definisjoner[ord] if (ord in definisjoner) else ord for ord in linje.strip().split(" ")[1:-1]]
    string = "".join(str(ord) for ord in liste)
    try:
        return linje[5:].strip() + " " + keyOfValue(definisjoner, eval(string))
    except:
        return linje[5:].strip() + " unknown"


def keyOfValue(dict1, value):
    for key in dict1.keys():
        if dict1[key] == value:
            return key



def main():
    linjer = [linje for linje in sys.stdin]

    definisjoner = {}

    for linje in linjer:
        ord = linje.strip().split(" ")

        if ord[0] == "calc":
            print(calc(linje, definisjoner))

        elif ord[0] == "def":
            definisjoner[ord[1]] = int(ord[2])

        elif ord[0] == "clear":
            definisjoner = {}
main()
