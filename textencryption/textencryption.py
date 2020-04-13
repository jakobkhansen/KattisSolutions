import sys

def textencryption(lines):
    retString = ""
    for i in range(0, len(lines), 2):

        n = int(lines[i].split(" ")[0])

        if (n == 0):
            break

        clear = lines[i+1].replace(" ", "").upper()

        retString += encrypt(clear, n) + "\n"

    return retString.strip()

def encrypt(clear, n):
    length = len(clear)

    if length <= n:
        return clear

    encrypted = [""]*length
    counter = 0
    startChar = 0

    for letter in clear:
        encrypted[counter] = letter
        counter += n
        if counter >= length:
            startChar += 1
            counter = startChar % length


    return "".join(encrypted).strip()


def main():
    lines = [line.strip() for line in sys.stdin]
    print(textencryption(lines))
main()
