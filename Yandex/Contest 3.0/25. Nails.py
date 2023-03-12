n = int(input())
lst = [int(i) for i in input().rstrip().split()]
lst.sort()
dp = [0] * n
dp[1] = lst[1] - lst[0]
if n > 2:
    dp[2] = lst[2] - lst[0]
    for i in range(3, n):
        dp[i] = min(dp[i - 2], dp[i - 1]) + lst[i] - lst[i - 1]
print(dp[n - 1])
