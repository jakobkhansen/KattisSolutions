import sys

def nastyhacks(lines):
    lines = lines[1:]

    streng = []
    for i in lines:
        values = [int(x) for x in i.split(" ")]
        if values[0] < values[1] - values[2]:
            streng.append("advertise")
        elif values[0] > values[1] - values[2]:
            streng.append("do not advertise")
        else:
            streng.append("does not matter")

    return "\n".join(streng)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(nastyhacks(lines))
main()
