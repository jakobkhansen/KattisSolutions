import sys

def Pot(lines): 
    numsList = [tall for tall in lines[1:]]

    finalNum = 0

    for num in numsList:
        power = int(num[-1])
        num = int(num[:-1])
        finalNum = finalNum + (num ** power)
    return finalNum

def main():
    lines = [line.strip() for line in sys.stdin]

    print(Pot(lines))
main()
