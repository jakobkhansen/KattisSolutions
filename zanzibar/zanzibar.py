import sys

def zanzibar(lines):
    for case in lines[1:]:
        spl = case.split()
        imports = 0
        for i in range(len(spl)-1):
            curr = int(spl[i])
            next = int(spl[i+1])

            max_next = curr*2
            imported = next - max_next
            imports += 0 if imported < 0 else imported
        print(imports)



def main():
    lines = [line.strip() for line in sys.stdin]
    (zanzibar(lines))
main()
