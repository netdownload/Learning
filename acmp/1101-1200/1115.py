# https://acmp.ru/asp/do/?main=task&id_course=1&id_section=1&id_topic=27&id_problem=158

# Количество обиженных школьников = n-(a % n), но если все поделилось по ровну, то формула не работает, либо
# использовать условие, либо еще раз вщять остаток от деления n-(a % n)) % n

n, a = map(int, input().split())
print((a//n), (a % n), (n-(a % n)) % n)
