length, jumps = map(int, input().split(' '))

if length == 1:
    print(length)
elif jumps == 1:
    print(length-1)
elif jumps >= 2:
    ans = [0] * length
    ans[0] = 1
    ans[1] = 1
    for n in range(2, jumps):
        ans[n] = ans[n-1] + ans[n-2]
    for j in range(jumps, length, 1):
        for i in range(jumps):
            ans[j] += ans[j-i-1]
    print(ans[length-1])
