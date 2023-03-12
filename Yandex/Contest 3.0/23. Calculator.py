n = int(input())
a = [0] * (n + 1)
a[1] = 0
for i in range(2, n + 1):
    minimal = a[i - 1] + 1
    if i % 2 == 0:
        minimal = min(minimal, a[i // 2] + 1)
    if i % 3 == 0:
        minimal = min(minimal, a[i // 3] + 1)
    a[i] = minimal

operations = []
operations.append(1)
i = n
while i > 1:
    if a[i] == (a[i-1]+1):
        operations.insert(1, 1)
        i -= 1
        continue
    if i%2 == 0 and a[i] == a[i//2]+1:
        operations.insert(1, 2)
        i //= 2
        continue
    operations.insert(1, 3)
    i //= 3
print(a[n])
ans = []
t = 0
for j in range(len(operations)):
    if operations[j] == 1:
        t = t + 1
        ans.append(t)
    if operations[j] == 2:
        t = t * 2
        ans.append(t)
    if operations[j] == 3:
        t = t * 3
        ans.append(t)
print(*ans)
