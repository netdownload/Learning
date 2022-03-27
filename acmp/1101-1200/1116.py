# https://acmp.ru/asp/do/?main=task&id_course=1&id_section=1&id_topic=28&id_problem=159


h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())
print((h2-h1)*3600 +(m2-m1)*60+(s2-s1))