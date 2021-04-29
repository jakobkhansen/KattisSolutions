def main():
    n = int(input())
    array = [int(x) for x in input().split()]
    biggest_left = array[0]
    smallest_right = array[n-1]

    good_left = [False]*n

    for i in range(n):
        if biggest_left <= array[i]:
            good_left[i] = True
            biggest_left = array[i]

    num_good = 0
    for i in range(n-1, -1, -1):
        if smallest_right >= array[i]:
            if good_left[i]:
                num_good += 1
            smallest_right = array[i]
    print(num_good)

if __name__ == "__main__":
    main()
