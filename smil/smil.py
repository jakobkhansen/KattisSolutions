import sys

def smil(lines):
    for i, letter in enumerate(lines[0]):
        if letter == ':' or letter == ';':
            try:
                if lines[0][i+1] == ')':
                    print(i)
                elif lines[0][i+1] == '-' and lines[0][i+2] == ')':
                    print(i)
            except:
                continue




def main():
    lines = [line.strip() for line in sys.stdin]
    smil(lines)
main()
