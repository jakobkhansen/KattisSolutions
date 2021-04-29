import sys
import math

def logo(lines):
    cases = int(lines[0])
    index = 1
    for i in range(cases):
        num_moves = int(lines[index])
        x,y = [0,0]
        angle = 0
        for i in range(index+1, index+num_moves+1):
            command, num = lines[i].split(" ")[0], lines[i].split(" ")[1]
            num = int(num)
            if command == "fd":
                x = x + math.cos(math.radians(angle))*num
                y = y + math.sin(math.radians(angle))*num
            elif command == "bk":
                x = x - math.cos(math.radians(angle))*num
                y = y - math.sin(math.radians(angle))*num
            elif command == "lt":
                angle = abs((angle + num) % 360)
            elif command == "rt":
                angle = abs((angle - num) % 360)
        distance = math.sqrt(x**2+y**2)
        print(round(distance))




        index += num_moves+1


def main():
    lines = [line.strip() for line in sys.stdin]
    (logo(lines))
main()
