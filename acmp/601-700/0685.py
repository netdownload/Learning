# https://acmp.ru/?main=task&id_task=685


a1, a2, a3, b1, b2, b3 = map(int, input().split())
print(max(a1, a2, a3)*max(b1, b2, b3)+min(a1, a2, a3)*min(b1, b2, b3) + 
      (a1+a2+a3-max(a1, a2, a3)-min(a1, a2, a3))*(b1+b2+b3-max(b1, b2, b3)-min(b1, b2, b3)))
