import sys

def nop(lines):
    mem = [char for char in lines[0]]
    num_nop = 0
    curr_instruction = 0
    next_instruction = 1
    while next_instruction < len(mem):
        while next_instruction < len(mem) and not mem[next_instruction].isupper():
            next_instruction += 1

        if next_instruction >= len(mem):
            break
        size = next_instruction - curr_instruction

        # print(size)
        # print(4-(size % 4))
        # print()
        num_nop += 0 if (size % 4) == 0 else 4-(size % 4)

        curr_instruction = next_instruction
        next_instruction += 1



    return num_nop


def main():
    lines = [line.strip() for line in sys.stdin]
    print(nop(lines))
main()
