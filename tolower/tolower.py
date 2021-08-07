import sys

def tolower(lines):
    P, T = [int(x) for x in lines[0].split()]
    passed = 0
    for i in range(P):
        flag = True
        for j in range(T):
            line = list(lines[i*T + j + 1])
            line[0] = line[0].lower()
            if not str(line).islower():
                flag = False
                break
        if flag:
            passed += 1
    return passed
        



def main():
    lines = [line.strip() for line in sys.stdin]
    print(tolower(lines))
main()
