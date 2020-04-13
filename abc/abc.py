import sys

def abc(lines):
    array = sorted([int(x) for x in lines[0].split(" ")])
    dict_order = order()
    new_array = [""]*3
    for index, letter in enumerate(lines[1]):
        new_array[index] = str(array[dict_order[letter]])

    return " ".join(new_array)


def order():
    order = {}
    order["A"] = 0
    order["B"] = 1
    order["C"] = 2
    return order

def main():
    lines = [line.strip() for line in sys.stdin]
    print(abc(lines))
main()
