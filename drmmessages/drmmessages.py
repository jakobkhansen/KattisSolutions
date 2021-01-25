import sys
import string

def drmmessages(lines):
    alphabet = string.ascii_uppercase


    rotValues = {}
    rotValuesReversed = {}
    for i,letter in enumerate(alphabet):
        rotValues[letter] = i
        rotValuesReversed[i] = letter

    message = lines[0]
    mid = len(message) // 2

    firstHalf = message[:mid]
    secondHalf = message[mid:]

    sumFirst = sum([rotValues[x] for x in firstHalf])
    sumSecond = sum([rotValues[x] for x in secondHalf])

    newFirst = ""
    for i, letter in enumerate(firstHalf):
        newVal = (rotValues[letter] + sumFirst) % len(rotValues.keys())
        newFirst += rotValuesReversed[newVal]
    firstHalf = newFirst

    newSecond = ""
    for i, letter in enumerate(secondHalf):
        newVal = (rotValues[letter] + sumSecond) % len(rotValues.keys())
        newSecond += rotValuesReversed[newVal]
    secondHalf = newSecond

    resultString = ""

    for i, letter in enumerate(firstHalf):
        valSecond = rotValues[secondHalf[i]]
        newCharVal = (rotValues[letter] + valSecond) % len(rotValues.keys())
        resultString += rotValuesReversed[newCharVal]
    return resultString


def main():
    lines = [line.strip() for line in sys.stdin]
    print(drmmessages(lines))
main()
