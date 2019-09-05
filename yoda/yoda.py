import sys

def yoda(lines):
    word1 = "".join(reversed(lines[0]))
    word2 = "".join(reversed(lines[1]))

    shortest = min(len(word1), len(word2))
    for i in range(shortest):
        num1 = int(word1[i])
        num2 = int(word2[i])

        if num1 < num2:
            tmp = list(word1)
            tmp[i] = ' '
            word1 = "".join(tmp)

        elif num2 < num1:
            tmp = list(word2)
            tmp[i] = ' '
            word2 = "".join(tmp)
    word1 = "".join(reversed(word1)).replace(" ", "")
    word2 = "".join(reversed(word2)).replace(" ", "")

    if word1 == "":
        word1 = "YODA"
    if word2 == "":
        word2 = "YODA"

    if all(char == '0' for char in word1):
        word1 = "0"

    if all(char == '0' for char in word2):
        word2 = "0"

    return word1 + "\n" + word2



def main():
    lines = [line.strip() for line in sys.stdin]
    print(yoda(lines))
main()
