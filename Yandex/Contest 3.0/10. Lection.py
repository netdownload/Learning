i = input()

dct = {}

for _ in range(len(i)):
    num = (_ + 1)*(len(i) - _)
    if dct.get(i[_]) is None:
        dct[i[_]] = num
    else:
        dct[i[_]] += num

for key in sorted(dct.keys()):
    print(f'{key}: {dct[key]}')
