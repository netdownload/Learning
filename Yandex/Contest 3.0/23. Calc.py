num = int(input())

a = [0] * (num + 1)  # для каждого числа пока заполняем по 0 операций
a[1] = 0  # продублирую для наглядности чтобы получить 1 нужно 0 операций

for n in range(2, num + 1):  # для каждого числа из диапазона
    minimal = a[n - 1] + 1  # смотрим сколько потребовалось операций для предыдущего и прибавляем
    if n % 2 == 0:
        minimal = min(minimal, a[n // 2] + 1)  # сравниваем сколько операций потребовалось для n//2+1
    if n % 3 == 0:
        minimal = min(minimal, a[n // 3] + 1)  # аналогично
    a[n] = minimal  # заполняем вместо 0 количество операций
print(a)
print(a[num])
operations = []
i = num
while i > 1:
    if a[i] == (a[i-1]+1):
        operations.insert(0, 1)
        i -= 1
        continue
    if i%2 == 0 and a[i] == a[i//2]+1:
        operations.insert(0, 2)
        i //= 2
        continue
    operations.insert(0, 3)
    i //= 3
print(operations)