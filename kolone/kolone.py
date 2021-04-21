import sys

def kolone(lines):
    DIR_LEFT = True
    DIR_RIGHT = False

    left = lines[1][::-1]
    right = lines[2]

    directions = {}

    for letter in left:
        directions[letter] = DIR_RIGHT

    for letter in right:
        directions[letter] = DIR_LEFT

    row = list(left + right)

    iterations = int(lines[-1])
    for _ in range(iterations):
        moved = {}
        for j in range(len(row)-1):
            if directions[row[j]] == DIR_RIGHT and directions[row[j+1]] == DIR_LEFT and not moved.get(row[j], False):
                moved[row[j]] = True
                temp = row[j]
                row[j] = row[j+1]
                row[j+1] = temp
                                                
    return "".join(row)



def main():
    lines = [line.strip() for line in sys.stdin]
    print(kolone(lines))
main()
