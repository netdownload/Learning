n = int(input().rstrip())
path1 = list(map(int, input().rstrip().split(' ')))
siding = []
top = -1
next = 0
path2 = 1

while next != n or (top != -1 and siding[top] == path2):
    if top != -1 and (siding[top] == path2):
        top -= 1
        siding.pop()
        path2 += 1
    else:
        top += 1
        siding.append(path1[next])
        next += 1
if path2 == (n + 1):
    print('YES')
else:
    print('NO')
