n = input()
ans = ''
while len(n) >= 4:
    tmp = "," + n[-3:]
    ans = tmp + ans
    n = n[:len(n)-3]
ans = n[:3] + ans
print(ans)
