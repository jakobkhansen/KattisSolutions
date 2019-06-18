import sys

def tri(lines):
    numbers = [num for num in lines[0].split(" ")]
    operations = ["+", "-", "*", "/"]

    # Equals right
    for op in operations:
        string = numbers[0] + op + numbers[1] + "==" + numbers[2]
        if (eval(string)):
            return string.replace("=", "", 1)

    # Equals left
    for op in operations:
        string = numbers[0] + "==" + numbers[1] + op + numbers[2]
        if (eval(string)):
            return string.replace("=", "", 1)

def main():
    lines = [line.strip() for line in sys.stdin]
    print(tri(lines))
main()
