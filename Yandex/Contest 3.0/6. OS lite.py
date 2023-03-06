m = int(input())
n = int(input())

ans = [0]*n
os = []
for i in range(n):
    temp = list(map(int, input().split(" ")))
    os.append(temp)

for i in range(n):
    for j in range(n-1):
        print(os[i], os[j+1])
        if os[i][0] <= os[j+1][1] and os[j+1][0] <= os[i][1]:
            ans[i] = 0
        else:
            ans[i] = 1
    print(ans)
print(os)
print(ans)

