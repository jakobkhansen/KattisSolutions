import sys

subs = {
    "at":"@",
    "and":"&",
    "one":"1",
    "won":"1",
    "to":"2",
    "too":"2",
    "two":"2",
    "for":"4",
    "four":"4",
    "bea":"b",
    "be":"b",
    "bee":"b",
    "sea":"c",
    "see":"c",
    "eye":"i",
    "oh": "o",
    "owe": "o",
    "are": "r",
    "you": "u",
    "why": "y"
}

def iforaneye(lines):
    lines = lines[1:]
    retString = ""
    for line in lines:
        retString += substitute(line) + "\n"
    return retString.strip()


def substitute(line):
    newString = ""
    i = 0
    while i < len(line):
        if line[i].isspace():
            newString += line[i]
            i += 1
            continue

        words = []
        for word in subs.keys():
            potentialWord = line[i:i+len(word)]
            if potentialWord.lower() == word:
                words.append(potentialWord)
        if len(words) > 0:
            replacer = sorted(words, key=len)[-1]
            sub = subs[replacer.lower()]
            sub = sub[0].upper() + sub[1:] if replacer[0].isupper() else sub
            newString += sub
            i += len(replacer)
        else:
            newString += line[i]
            i += 1



    return newString


def main():
    lines = [line.strip() for line in sys.stdin]
    print(iforaneye(lines))
main()
