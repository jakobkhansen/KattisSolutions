import sys

def modulararithmetic(lines):
    i = 0
    n,t = None, None
    while n != 0 and t != 0:
        n,t = [int(x) for x in lines[i].split()]

        for j in range(i+1,i+t+1):
            operand1, op, operand2 = lines[j].split()
            if op == "/":
                print((int(operand1)*((int(operand2)**-1) % n)))
            else:
                print(eval(f"({lines[j]}) % {n}"))

        i += t+1


def main():
    lines = [line.strip() for line in sys.stdin]
    print(modulararithmetic(lines))
main()
