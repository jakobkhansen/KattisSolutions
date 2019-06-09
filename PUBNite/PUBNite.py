import sys

class Circle:
    def __init__(self, x, y, speed, radius, radius_end):
        self._position = [x, y]
        self._speed = speed
        self._radius = radius
        self._radius_end = radius_end

    def __str__(self):
        streng = str(self._position) + ", speed: " + str(self._speed)
        streng += ", radius: " + str(self._radius) + ", radius_end: " + str(self._radius_end)
        return streng

    def get_position(self):
        return self._position

    def get_speed(self):
        return self._speed

    def get_radius(self):
        return self._radius

    def get_radius_end(self):
        return self._radius

class Player:
    def __init__(self, x, y, speed):
        self._position = [x, y]
        self._speed = speed

    def __str__(self):
        return str(self._position) + ", " + str(self._speed)

    def get_position(self):
        return self._position

    def get_speed(self):
        return self._speed



def calc_lines(lines):
    line_circle = lines[0].split(" ")
    line_player = lines[1].split(" ")

    circle = Circle(line_circle[0], line_circle[1], line_circle[2], line_circle[3], line_circle[4])
    player = Player(line_player[0], line_player[1], line_player[2])

    print(circle)
    print(player)

def main():
    lines = [line for line in sys.stdin]

    print(calc_lines(lines))
main()
