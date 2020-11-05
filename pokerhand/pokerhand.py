import sys

def pokerhand(lines):
    power = {}
    for card in lines[0].split():
        rank = card[0]
        if rank in power:
            power[rank] += 1
        else:
            power[rank] = 1
    return power[max(power.keys(), key=power.get)]


def main():
    lines = [line.strip() for line in sys.stdin]
    print(pokerhand(lines))
main()
