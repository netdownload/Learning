# https://acmp.ru/index.asp?main=task&id_task=263


t, b, e = map(int, input().split())
print(min(t-abs(e-b)-1, abs(e-b)-1))
