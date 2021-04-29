import sys

def apaxiaaans(lines):
    name = [x for x in lines[0]]
    for i in range(len(name)):
        if i == 0:
            continue
        if i >= len(name):
            break

        while i < len(name) and name[i] == name[i-1]:
            name.pop(i)
    return "".join(name)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(apaxiaaans(lines))
main()
