num = int(input())
array = [int(x) - 1 for x in input().split()]
visited = [False]*num

swap_count = 0

for i in range(num):
    if visited[i]:
        continue
    curr_index = i
    while array[curr_index] != i:
        visited[curr_index] = True
        curr_index = array[curr_index]
        if visited[curr_index]:
            break
        swap_count += 1
print(swap_count)
