n, m = map(int, input().split())
food = [[0] * m for i in range(n)]
dp = [[0] * m for i in range(n)]

for i in range(n):
    food[i] = list(map(int, input().rstrip().split(' ')))

dp[0][0] = food[0][0]
for j in range(1, m):
    dp[0][j] = dp[0][j-1]+food[0][j]
for i in range(1, n):
    dp[i][0] = dp[i-1][0]+food[i][0]
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = min(dp[i][j-1], dp[i-1][j])+food[i][j]
print(dp[n-1][m-1])
