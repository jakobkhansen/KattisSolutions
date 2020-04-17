import sys

def basicprogramming1(lines):
    command = int(lines[0].split(" ")[1])
    array = [int(x) for x in lines[1].split(" ")]

    commands = [
        one,
        two,
        three,
        four,
        five,
        six,
        seven
    ]

    return commands[command-1](array)


def one(a):
    return "7"

def two(a): 
    if a[0] > a[1]:
        return "Bigger"

    if a[0] < a[1]:
        return "Smaller"

    return "Equal"

def three(a):
    return str(sorted(a[:3])[1])

def four(a):
    return str(sum(a))

def five(a):
    return str(sum([x for x in a if x % 2 == 0]))

def six(a):
    nums = [x % 26 for x in a]
    chars = [chr(num + 97) for num in nums]
    return "".join(chars)

def seven(a):
    visited = [0]*(len(a)+10)
    i = 0
    while 0 <= i < len(a):
        visited[i] = 1
        i = a[i]

        if visited[i] == 1:
            return "Cyclic"

        if i == len(a) - 1:
            return "Done"

    return "Out"



def main():
    lines = [line.strip() for line in sys.stdin]
    print(basicprogramming1(lines))
main()
