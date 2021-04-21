import sys

def eatingout(lines):
    m,a,b,c = [int(x) for x in lines[0].split(" ")]
    overlap = (a+b) - m if (a+b) - m >= 0 else 0
    c_overlap = m - (c + overlap)
    return "impossible" if c_overlap < 0 else "possible"



def main():
    lines = [line.strip() for line in sys.stdin]
    print(eatingout(lines))
main()
