import sys

def locustlocus(lines):
    lowest = sys.maxsize
    pairs = [[int(x) for x in y.split()] for y in lines[1:]]

    for pair in pairs:
        x,y = pair[1:]
        res = pair[0] + compute_lcm(x,y)
        lowest = res if res < lowest else lowest
    return lowest

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


def main():
    lines = [line.strip() for line in sys.stdin]
    print(locustlocus(lines))
main()
