import sys

def vauvau(lines):
    a,b,c,d = [int(x) for x in lines[0].split()]
    f_t = a+b
    s_t = c+d

    p,m,g = [int(x) for x in lines[1].split()]

    for p in [p,m,g]:
        p_t_1 = p % f_t
        p_t_2 = p % s_t
        # print(p, p_t_1, p_t_2)

        if p_t_1 != 0 and p_t_1 <= a and p_t_2 != 0 and p_t_2 <= c:
            print("both")
        elif (p_t_1 != 0 and p_t_1 <= a) or (p_t_2 != 0 and p_t_2 <= c):
            print("one")
        else:
            print("none")


def main():
    lines = [line.strip() for line in sys.stdin]
    vauvau(lines)
main()
