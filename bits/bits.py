import sys

def bits(lines):
    nums = [str(x) for x in lines][1:]
    retStr = []

    for num in nums:
        mostOnes = 0
        for i in range(1,len(num)+1):
            numStr = num[0:i]
            numBin = bin(int(numStr))[2:]
            numOnes = 0
            for bit in numBin:
                if bit == "1":
                    numOnes += 1
            mostOnes = numOnes if numOnes > mostOnes else mostOnes
        retStr.append(str(mostOnes))

    return "\n".join(retStr)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(bits(lines))
main()
