import sys

def echoechoecho(lines):
    word = lines[0]
    words = [word]*3
    return " ".join(words)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(echoechoecho(lines))
main()
