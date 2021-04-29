import sys

def warehouse(lines):
    cases = int(lines[0])
    ind = 1
    for _ in range(cases):
        toys = {}
        num_toys = int(lines[ind])

        for i in range(num_toys):
            name,num = lines[ind+i+1].split()
            if toys.get(name, False):
                toys.get(name)[1] += int(num)
            else:
                toys[name] = [name, int(num)]

        toy_list = sorted(toys.values(), key=lambda x: x[0])
        toy_list.sort(key=lambda x:x[1], reverse=True)
        print(len(toys.keys()))
        print("\n".join("{} {}".format(x[0],x[1]) for x in toy_list))

        ind += num_toys + 1


def main():
    lines = [line.strip() for line in sys.stdin]
    (warehouse(lines))
main()
