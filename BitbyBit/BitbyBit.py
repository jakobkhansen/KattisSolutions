import sys

def evalBits(commands):

    bits = "?"*32

    for command in commands:
        words = command.split(" ")

        commandSwitcher = {
            "SET" : setBit(command, bits),
            "CLEAR" : clearBit(command, bits),
            "AND" : andBit(command, bits),
            "OR" : orBit(command, bits)
        }


        bits = commandSwitcher.get(words[0], "No command")

    return bits

def setBit(command, bits):
    bit = int(command.split(" ")[1])

    newBitsList = list(bits)
    newBitsList[31-bit] = "1"

    return "".join(newBitsList)

def clearBit(command, bits):
    bit = int(command.split(" ")[1])

    newBitsList = list(bits)
    newBitsList[31-bit] = "0"

    return "".join(newBitsList)

def andBit(command, bits):
    try:
        bitXIndex = 31 - int(command.split(" ")[1])
        bitYIndex = 31 - int(command.split(" ")[2])

        newBitsList = list(bits)

        bitXValue = newBitsList[bitXIndex]
        bitYValue = newBitsList[bitYIndex]

        if bitXValue == "0" or bitYValue == "0":
            newBitsList[bitXIndex] = "0"

        elif bitXValue == "1" and bitYValue == "1":
            newBitsList[bitXIndex] = "1"

        else:
            newBitsList[bitXIndex] = "?"


        return "".join(newBitsList)
    except:
        return

def orBit(command, bits):
    try:
        bitXIndex = 31 - int(command.split(" ")[1])
        bitYIndex = 31 - int(command.split(" ")[2])

        newBitsList = list(bits)

        bitXValue = newBitsList[bitXIndex]
        bitYValue = newBitsList[bitYIndex]

        if bitXValue == "1" or bitYValue == "1":
            newBitsList[bitXIndex] = "1"

        elif bitXValue == "?" or bitYValue == "?":
            newBitsList[bitXIndex] = "?"

        else:
            newBitsList[bitXIndex] = "0"

        return "".join(newBitsList)
    except:
        return


def main():
    lines = [line.strip() for line in sys.stdin]
    output = ""

    while True:
        numCommands = int(lines[0])
        output += evalBits(lines[1:numCommands+1]) + "\n"
        lines = lines[numCommands+1:]

        if lines == ["0"]:
            break

    print(output)
main()
