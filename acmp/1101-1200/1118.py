# https://acmp.ru/asp/do/?main=task&id_course=1&id_section=1&id_topic=28&id_problem=161


t, d, n = map(int, input().split())
print(max(int(((t-d+d-n-1)//(d-n)+1)), 1))

t, d, n = map(int, input().split())
print(max(int(((t-n-1)//(d-n)+1)), 1))
