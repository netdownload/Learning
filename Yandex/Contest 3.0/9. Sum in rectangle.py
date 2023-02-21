n, m, k = map(int, input().rstrip().split(' '))

arr = []
prefix_sum1d = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    arr.append([])
    for j in map(int, input().rstrip().split(' ')):
        arr[i].append(j)

for i in range(n):
    for j in range(m):
        prefix_sum1d[i][j] = arr[i][j]
        if i:
            prefix_sum1d[i][j] += prefix_sum1d[i - 1][j]
        if j:
            prefix_sum1d[i][j] += prefix_sum1d[i][j -1]
        if i and j:
            prefix_sum1d[i][j] -= prefix_sum1d[i - 1][j - 1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().rstrip().split(' '))
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    sum = prefix_sum1d[x2][y2]
    if x1:
        sum -= prefix_sum1d[x1 - 1][y2]
    if y1:
        sum -= prefix_sum1d[x2][y1 - 1]
    if x1 and y1:
        sum += prefix_sum1d[x1 - 1][y1 - 1]
    print(sum)
