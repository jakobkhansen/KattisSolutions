import sys

def findR2(linjer):
    r1 = int(linjer[0].split(" ")[0])
    s = int(linjer[0].split(" ")[1])
    r2 = (s*2)-r1
    
    return r2



def main():
    linjer = [linje for linje in sys.stdin]

    print(findR2(linjer))

main()
