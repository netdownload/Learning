n = int(input())
p1 = list(map(int, input().rstrip().split(' ')))
m = int(input())
p2 = list(map(int, input().rstrip().split(' ')))
f = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if p1[i - 1] == p2[j - 1]:
            f[i][j] = f[i - 1][j - 1] + 1
        else:
            f[i][j] = max(f[i - 1][j], f[i][j - 1])

ans = []
i = n
j = m
while i > 0 and j > 0:
    if p1[i - 1] == p2[j - 1]:
        ans.append(p1[i - 1])
        i -= 1
        j -= 1
    elif f[i - 1][j] == f[i][j]:
        i -= 1
    else:
        j -= 1

print(*ans[::-1])
