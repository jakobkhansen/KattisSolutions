import sys

def skener(lines):
    r,c,z_r, z_c = [int(x) for x in lines[0].split(" ")]
    original = [list(x) for x in lines[1:]]
    new = [[' ' for _ in range(z_c*c)] for _ in range(z_r*r)]

    # print(new)
    for i in range(len(original)):
        for j in range(len(original[i])):
            for c in range(z_c):
                # print("c: " + original[i][j])
                # print(i, j, c)
                for r in range(z_r):
                    new[(i*z_r)+r][(j*z_c)+c] = original[i][j]
                # new[i*z_r][(j*z_c)+c] = original[i][j] 
                # print("r: " + original[i][j])
                # print(i, j, c)
                # print((i*z_r)+r, j)
            # print()
    print_matrix(new)

def print_matrix(matrix):
    out = ""
    for row in matrix:
        for char in row:
            out += char
        out += "\n"
    print(out.strip())

def main():
    lines = [line.strip() for line in sys.stdin]
    (skener(lines))
main()
