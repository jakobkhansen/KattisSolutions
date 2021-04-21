import sys

def forcedchoice(lines):
    n,p,s = [int(x) for x in lines[0].split(" ")]
    for line in lines[1:]:
        nums = [int(x) for x in line.split(" ")][1:]
        if p in nums:
            print("KEEP")
        else:
            print("REMOVE")



def main():
    lines = [line.strip() for line in sys.stdin]
    forcedchoice(lines)
main()
