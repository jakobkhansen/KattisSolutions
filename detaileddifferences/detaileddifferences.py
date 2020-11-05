import sys

def detaileddifferences(lines):
    retStr = []

    lines = lines[1:]
    for i in range(0, len(lines), 2):
        word1 = lines[i]
        word2 = lines[i+1]

        result = "{}\n{}\n".format(word1, word2)
        for j in range(len(word1)):
            if word1[j] == word2[j]:
                result += "."
            else:
                result += "*"
        retStr.append(result + "\n")
    return "\n".join(retStr).strip()


def main():
    lines = [line.strip() for line in sys.stdin]
    print(detaileddifferences(lines))
main()
