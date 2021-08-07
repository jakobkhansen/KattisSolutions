import sys

def proofs(lines):
    lines = lines[1:]
    axioms = {}

    for i,line in enumerate(lines):
        sides = line.split("->")
        if sides[0] == "":
            for axiom in sides[1].split():
                axioms[axiom] = True
        else:
            if all([True if x in axioms else False for x in sides[0].split()]):
                for axiom in sides[1].split():
                    axioms[axiom] = True
            else:
                return i+1
    return "correct"




def main():
    lines = [line.strip() for line in sys.stdin]
    print(proofs(lines))
main()
