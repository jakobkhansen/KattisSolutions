import sys

def erase(lines):
    num_deletions = int(lines[0]) % 2
    bits = [int(y) for y in lines[1]]
    answer = [int(x) for x in lines[2]]

    for i in range(len(bits)):
        bits[i] = (bits[i] + num_deletions) % 2
    return "Deletion succeeded" if bits == answer else "Deletion failed"



def main():
    lines = [line.strip() for line in sys.stdin]
    print(erase(lines))
main()
