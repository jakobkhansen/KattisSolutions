import sys

def cd(lines):
    i = 0
    while i < len(lines):
        n,m = [int(x) for x in lines[i].split()]
        if n == 0 and m == 0:
            break

        l = i+1
        r = i+n+1

        sum = 0
    
        # print(i+n+1, i+n+m+1)
        while l < i+n+1 and r < i+n+m+1:
            # print(lines[l],lines[r])
            while int(lines[l]) < int(lines[r]):
                l += 1
            while int(lines[r]) < int(lines[l]):
                r += 1

            if l < i+n+1 and r < i+n+m+1:
                if int(lines[l]) == int(lines[r]):
                    sum += 1
                    l += 1
                    r += 1


        print(sum)




        i += n+m+1


def main():
    lines = [line.strip() for line in sys.stdin]
    cd(lines)
main()
