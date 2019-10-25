import sys

def fourthought(lines):
    operators = ["*", "+", "-", "/"]
    expressions = {}
    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                expression = "4 {} 4 {} 4 {} 4".format(op1, op2, op3)
                expression_sum = int(eval(expression))
                expressions[expression_sum] = expression

    ret = []
    for line in lines[1:]:
        if int(line) in expressions:
            ret.append(expressions[int(line)] + " = " + line)
        else:
            ret.append("no solution")
    return "\n".join(ret)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(fourthought(lines))
main()
