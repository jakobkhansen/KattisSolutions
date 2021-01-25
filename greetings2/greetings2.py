import sys

def greetings2(lines):
    greeting = lines[0]

    e = (len(greeting) - 2)*2

    return "h" + "e"*e + "y"



def main():
    lines = [line.strip() for line in sys.stdin]
    print(greetings2(lines))
main()
