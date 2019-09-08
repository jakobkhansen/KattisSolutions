import sys

def simon(lines):
    ret = []
    for line in lines[1:]:
        sentence = line.split(" ")
        if len(sentence) > 1:
            if sentence[0] + " " + sentence[1] == "simon says":
                ret.append(" ".join(sentence[2:]))
                continue
        ret.append("")
    return "\n".join(ret)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(simon(lines))
main()
