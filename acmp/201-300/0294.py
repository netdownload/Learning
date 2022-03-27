# https://acmp.ru/?main=task&id_task=294


k1, l1, m1 = map(int, input().split())
k2, l2, m2 = map(int, input().split())
print(int(k1*l1/100*m1+k2*l2/100*m2+((k1-k1*l1/100)-min(k1-k1*l1/100, k2-k2*l2/100))*m1+((k2-k2*l2/100)-min(k1-k1*l1/100, k2-k2*l2/100))*m2))