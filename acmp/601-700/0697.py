# https://acmp.ru/?main=task&id_task=697

# a /^ b = (a+b-1)//b

l, w, h = map(int, input().split())
print(((2*l*h + 2*w*h) + 16-1)//16)