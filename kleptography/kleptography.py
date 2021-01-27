import sys
import string

def kleptography(lines):
    alpha = string.ascii_lowercase
    alphaNums = {alpha[i]:i for i in range(len(alpha))}
    alphaNumsRev = {alphaNums[i]:i for i in alphaNums.keys()}

    keyStart = lines[1]
    n = len(lines[1])

    text = list(lines[2])

    for i in range(n+1):
        text[-i] = keyStart[-i]

    for i in range(len(text)-n-1, 0, -1):
        bi = text[i]
        ki = text[i+n]

        bi_n = alphaNums[bi]
        ki_n = alphaNums[ki]

        # print(ai_n, ki_n)

        ai_n = (bi_n - ki_n) % 26

        print(alphaNumsRev[ai_n])



def main():
    lines = [line.strip() for line in sys.stdin]
    print(kleptography(lines))
main()
