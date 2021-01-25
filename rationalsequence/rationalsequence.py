import sys

class RationalNumber:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def isLeftChild(self):
        return p < q

    def isRightChild(self):
        return p > q

    def __repr__(self):
        return "{}/{}".format(self.p, self.q)

    def __eq__(self, other):
        return self.p == other.p and self.q == other.q

    def getParent(self):
        return 


def rationalsequence(lines):
    for num in lines[1:]:
        string = num.split(" ")[1].split("/")
        rationalNum = RationalNumber(int(string[0]), int(string[1]))

        if 


def main():
    lines = [line.strip() for line in sys.stdin]
    print(rationalsequence(lines))
main()
