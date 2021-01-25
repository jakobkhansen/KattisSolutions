import sys

def backspace(lines):
    currentStr = lines[0]
    output = []
    stored = 0

    for char in reversed(currentStr):
        if char == "<":
            stored += 1
        else:
            if stored > 0:
                stored -= 1
            else:
                output.append(char)

    return "".join(reversed(output))




def main():
    lines = [line.strip() for line in sys.stdin]
    print(backspace(lines))
main()
