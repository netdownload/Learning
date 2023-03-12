# n, m = map(int, input().split())
# lst = [list(map(int,input().split()))for i in range(n)]
# ans = [[0]*(m+1) for i in range(n+1)]
# route = []
# ans[1][1] = lst[0][0]
# for i in range(1, n+1):
#     ans[i][1] = lst[i-1][0]+ans[i-1][1]
# for j in range(1, n+1):
#     ans[1][j] = lst[0][j-1]+ans[1][j-1]
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         ans[i][j] = lst[i-1][j-1]+max(ans[i-1][j], ans[i][j-1])
# i, j = n, m
# while i >= 1 and j >= 1:
#     if ans[i-1][j] > ans[i][j-1]:
#         route.append('D')
#         i -= 1
#     else:
#         route.append('R')
#         j -= 1
# print(ans[-1][-1])
# print(' '.join(route[-2::-1]))

n, m = map(int,input().split())
arr, ans_lst =[list(map(int,input().split())) for i in range(n)], []
count1, count2 = 0, 0
for i in range(n):
    for j in range(m):
        if i >= 1 and j >= 0: count1 = arr[i - 1][j]
        if i >= 0 and j >= 1: count2 = arr[i][j - 1]
        arr[i][j] += max(count1, count2)
        count1, count2 = 0, 0
i, j = n - 1, m - 1
while i != 0 or j != 0:
    if j >= 1 and i >= 1:
        if arr[i][j - 1] > arr[i - 1][j]:ans_lst.append("R")
        else:ans_lst.append("D")
    else:
        if j >= 1:ans_lst.append("R")
        else:ans_lst.append("D")
    if ans_lst[-1] == "D":i -= 1
    else:j -= 1
print(arr[-1][-1])
print(*(ans_lst[::-1]))
