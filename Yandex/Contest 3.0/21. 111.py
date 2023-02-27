i = int(input().strip())
dp = [0]*(i+3)
dp[0] = 2
dp[1] = 4
dp[2] = 7

if i <= 3:
    print(dp[i - 1])
else:
    for k in range(3, i, 1):
        dp[k] = dp[k - 1] + dp[k - 2] + dp[k-3]
    print(dp[i-1])
