import sys

def t9spelling(lines):
    letter_to_key = {
        'a':2,
        'b':22,
        'c':222,
        'd':3,
        'e':33,
        'f':333,
        'g':4,
        'h':44,
        'i':444,
        'j':5,
        'k':55,
        'l':555,
        'm':6,
        'n':66,
        'o':666,
        'p':7,
        'q':77,
        'r':777,
        's':7777,
        't':8,
        'u':88,
        'v':888,
        'w':9,
        'x':99,
        'y':999,
        'z':9999,
        ' ':0
    }
    for i,line in enumerate(lines[1:]):
        out = ""
        for letter in line:
            appendee = str(letter_to_key[letter])
            if len(out) > 0 and appendee[0] == out[-1]:
                out += ' '
            out += appendee
        out = f"Case #{i+1}: {out}"
        print(out)




def main():
    lines = [line.strip() for line in sys.stdin]
    t9spelling(lines)
main()
