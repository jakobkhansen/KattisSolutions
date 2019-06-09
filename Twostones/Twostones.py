import sys

def find_winner(lines):
    num = int(lines[0])
    if num % 2 == 0:
        return "Bob"
    return "Alice"

def main():
    lines = [line for line in sys.stdin]
    print(find_winner(lines))
main()
