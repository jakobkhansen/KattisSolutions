import sys

def convertNumbers(stringArray):

    switcherTeens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"

    }

    switcherTens = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }

    switcherOnes = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    new_stringArray = []

    for linje in stringArray:
        new_linje = ""
        for word in linje.split(" "):
            if word.isdigit():
                num = word
                stringNum = ""
                if len(num) == 2 and num[0] == "1":
                    stringNum += str(switcherTeens.get(int(num)))
                elif len(num) == 2:
                    stringNum += str(switcherTens.get(int(num[0])))
                    if num[1] != "0":
                        stringNum += "-"
                    stringNum += str(switcherOnes.get(int(num[1])))
                else:
                    if num[0] == "0":
                        stringNum += "zero"
                    else:
                        stringNum += str(switcherOnes.get(int(num)))

                new_linje += (stringNum) + " "

            else:
                new_linje += (word) + " "

        new_linje = new_linje.capitalize()
        new_stringArray.append(new_linje)

    return "\n".join(new_stringArray)


def main():
    linjer = [linje.strip() for linje in sys.stdin]
    print(convertNumbers(linjer))
main()
