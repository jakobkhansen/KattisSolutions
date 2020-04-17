import sys

def whatdoesthefoxsay(lines):
    numCases = int(lines[0].split(" ")[0])

    lines = lines[1:]
    retString = []
    for i in range(numCases):
        text = lines[0]
        lines = lines[1:]
        words = []
        while lines[0] != "what does the fox say?":
            words.append(lines[0].split(" ")[-1])
            lines = lines[1:]

        foxsays = [word for word in text.split(" ") if word not in words]

        retString.append(" ".join(foxsays))
        lines = lines[1:]

    return "\n".join(retString)


def main():
    lines = [line.strip() for line in sys.stdin]
    print(whatdoesthefoxsay(lines))
main()
