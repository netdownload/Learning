m, n, k = map(int, input().split(' '))

arr = []
r = 0
for i in range(m):
    arr.append([])
    for j in range(n):
        arr[i].append(r)
        r += 1
print(arr)
