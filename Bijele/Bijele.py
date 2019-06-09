import sys

def missing_pieces(lines):
    default_set = [1, 1, 2, 2, 2, 8]
    current_set = [int(val) for val in lines[0].strip().split(" ")]
    missing_pieces = []

    for i in range(len(default_set)):
        missing_pieces.append(str(default_set[i] - current_set[i]))
    return " ".join(missing_pieces)

def main():
    lines = [line for line in sys.stdin]

    print(missing_pieces(lines))
main()
