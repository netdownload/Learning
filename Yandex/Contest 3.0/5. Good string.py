i = int(input())
curr = int(input())
ans = 0
for n in range(i - 1):
    next = int(input())
    if curr <= next:
        ans += curr
    else:
        ans += next
    curr = next

print(ans)
