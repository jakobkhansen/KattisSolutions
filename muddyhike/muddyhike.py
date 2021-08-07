import sys

def muddyhike(lines):
    r,c = [int(x) for x in lines[0].split()]
    map = [[int(x) for x in y.split()] for y in lines[1:]]
    deepest = [[0]*len(x) for x in map]

    for i in range(r):
        deepest[i][-1] = map[i][-1]

    print(print_arr(deepest))
    for i in range(c-2,-1, -1):
        for j in range(r):
            smallest = max(map[j][i], deepest[j][i+1])
            travel_up_cost = 0
            for k in range(j, -1, -1):
                travel_up_cost = map[k][i] if map[k][i] > travel_up_cost else travel_up_cost
                if travel_up_cost < smallest and deepest[k][i+1] < smallest:
                    smallest = max(travel_up_cost, map[k][i+1])

            travel_down_cost = 0
            for k in range(j, r):
                travel_down_cost = map[k][i] if map[k][i] > travel_down_cost else travel_down_cost
                if travel_down_cost < smallest and deepest[k][i+1] < smallest:
                    smallest = max(travel_down_cost, deepest[k][i+1])
            deepest[j][i] = smallest 

        print(print_arr(deepest))
            
    min_deep = deepest[0][0]
    for i in range(r):
        min_deep = deepest[i][0] if deepest[i][0] < min_deep else min_deep


    return min_deep



def print_arr(arr):
    string = "["
    for row in arr:
        string += "\n[ "
        for elem in row:
            string += str(elem) + " "
        string += "]"
    return string + "\n]"




def main():
    lines = [line.strip() for line in sys.stdin]
    print(muddyhike(lines))
main()
