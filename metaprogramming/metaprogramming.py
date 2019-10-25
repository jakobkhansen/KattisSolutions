import sys

def metaprogramming(lines):
    definitions = {}

    ret = ""

    for line in lines:
        words = line.split(" ")

        if (words[0] == "define"):
            definitions[words[2]] = int(words[1])

        elif (words[0] == "eval"):
            string = str(evaluate(definitions, words))
            ret += string.lower() + "\n"

    return ret.strip()




def evaluate(definitions, expression):
    keyword1 = expression[1]
    keyword2 = expression[3]
    operator = expression[2]

    if (operator == "="):
        operator = "=="

    if (definitions.get(keyword1) is None or definitions.get(keyword2) is None):
        return "undefined"

    return eval("{} {} {}".format(definitions[keyword1], operator, definitions[keyword2]))


def main():
    lines = [line.strip() for line in sys.stdin]
    print(metaprogramming(lines))
main()
