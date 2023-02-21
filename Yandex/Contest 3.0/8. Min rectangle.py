k = int(input())
xs = []
ys = []
for _ in range(k):
    x, y = map(int, input().rstrip().split(' '))
    xs.append(x)
    ys.append(y)

print(f'{min(xs)} {min(ys)} {max(xs)} {max(ys)}')
