import sys

def baloni(lines):
    balloons = [int(x) for x in lines[1].split(" ")]
    counter = 0
    while balloons != []:
        height = balloons[0]-1
        balloons.pop(0)
        counter += 1

        index = 0
        while height > 0 and index < len(balloons):
            if balloons[index] == height:
                balloons.pop(index)
                height -= 1
                index -= 1
            index += 1
    return counter



def main():
    lines = [line.strip() for line in sys.stdin]
    print(baloni(lines))
main()
