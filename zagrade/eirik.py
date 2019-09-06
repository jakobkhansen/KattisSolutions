import sys

def remove(string, expressions, index):
    string = string[:index] + string[(index + 1):]
    counter = 0
    while index < len(string):
        if string[index] == '(':
            counter +=1

        if string[index] == ')':
            if counter == 0:
                string = string[:index] + string[(index + 1):]
                break
            else:
                counter -= 1


        index += 1

    return string

def compute(string, expressions, i):
    expressions.add(string)
    while i < len(string):
        if string[i] == '(':
            s_2 = remove(string, expressions, i)
            compute(string, expressions, i + 1)
            compute(s_2, expressions, i)
            return

        i += 1

line = sys.stdin.readline().strip('\n')
expressions = set()

compute(line, expressions, 0)
expressions = list(expressions)
expressions = sorted(expressions)

for x in expressions:
    if x != line:
        print(x)
