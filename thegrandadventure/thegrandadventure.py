import sys

def thegrandadventure(lines):
    adventures = lines[1:]
    retString = ""
    for adv in adventures:
        retString += evaluateAdventure(adv) + "\n"
    return retString.strip()

def evaluateAdventure(adv):
    backpack = []
    actions = {
        ".": lambda : True,
        "$": lambda : backpack.append("$") == None,
        "|": lambda : backpack.append("|") == None,
        "*": lambda : backpack.append("*") == None,
        "t": lambda : len(backpack) > 0 and backpack.pop() == "|",
        "j": lambda : len(backpack) > 0 and backpack.pop() == "*",
        "b": lambda : len(backpack) > 0 and backpack.pop() == "$"
    }
    for symbol in adv:
        if actions[symbol]() is False:
            return "NO"

    if len(backpack) == 0:
        return "YES"

    return "NO"



def main():
    lines = [line.strip() for line in sys.stdin]
    print(thegrandadventure(lines))
main()
