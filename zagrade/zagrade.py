import sys
from itertools import combinations

def zagrade(lines):
    expression = lines[0]
    brackets = find_brackets(expression)
    combos = []
    for i in range(1, len(brackets)+1):
        combos.append(list(combinations(brackets, i)))

    return_array = []
    for i in combos:
        # print(i)
        for j in i:
            # print(j)
            current_exp = expression
            for x in j:
                current_exp = list(current_exp)
                current_exp[x[0]] = ' '
                current_exp[x[1]] = ' '
            current_exp = "".join(current_exp).replace(" ", "")
            return_array.append(current_exp)

    return_array = list(set(return_array))
    return "\n".join(sorted(return_array))

def find_brackets(expression):
    brackets = []
    used = []
    for i in range(len(expression)):
        if expression[i] == '(':
            right_counter = 0
            for j in range(i+1, len(expression)):
                if expression[j] == '(':
                    right_counter += 1
                elif expression[j] == ')' and right_counter > 0:
                    right_counter -= 1
                elif expression[j] == ')' and j not in used:
                    brackets.append((i, j))
                    used.append(j)
                    break
    return brackets

def main():
    lines = [line.strip() for line in sys.stdin]
    print(zagrade(lines))
main()
