import sys

def soundex(lines):
    soundex = {
        "B": "1",
        "F": "1",
        "P": "1",
        "V": "1",
        "C": "2",
        "G": "2",
        "J": "2",
        "K": "2",
        "Q": "2",
        "S": "2",
        "X": "2",
        "Z": "2",
        "D": "3",
        "T": "3",
        "L": "4",
        "M": "5",
        "N": "5",
        "R": "6"
    }

    ret = []

    for word in lines:
        wordSum = ""
        lastChar = ""

        for char in word:
            char = soundex.get(char, "")

            if char != lastChar:
                wordSum += char
            lastChar = char
        ret.append(wordSum)

    return "\n".join(ret)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(soundex(lines))
main()
