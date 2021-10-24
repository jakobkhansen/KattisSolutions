import sys

class Circle:
    def __init__(self, x, y, r) -> None:
        self.x = x
        self.y = y
        self.r = r

def grazedgrains(lines):
    circles = []
    for line in lines[1:]:
        nums = [int(x) for x in line.split()]
        circles.append(Circle(*nums))
    
    x_min = min(c.x - c.r for c in circles)
    x_max = max(c.x + c.r for c in circles)
    y_min = min(c.y - c.r for c in circles)
    y_max = max(c.y + c.r for c in circles)
 
    box_side = 500
 
    dx = (x_max - x_min) / box_side
    dy = (y_max - y_min) / box_side
 
    count = 0
 
    for r in range(box_side):
        y = y_min + r * dy
        for c in range(box_side):
            x = x_min + c * dx
            if any((x-circle.x)**2 + (y-circle.y)**2 <= (circle.r ** 2)
                   for circle in circles):
                count += 1
 
    return count * dx * dy


def main():
    lines = [line.strip() for line in sys.stdin]
    print(grazedgrains(lines))
main()
