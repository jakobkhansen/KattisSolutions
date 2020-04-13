import sys

def fiftyshades(lines):

    counter = 0
    for line in lines:
        if "pink" in line.lower():
            counter += 1

        elif "rose" in line.lower():
            counter += 1

    if counter == 0:
        return "I must watch Star Wars with my daughter"

    return counter



def main():
    lines = [line.strip() for line in sys.stdin]
    print(fiftyshades(lines))
main()
