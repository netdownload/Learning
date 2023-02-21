first = list(map(int, input().rstrip().split(' ')))
second = list(map(int, input().rstrip().split(' ')))
i = 0

while i <= 1000000 and len(first) != 0 and len(second) != 0:
    first_card = first.pop(0)
    second_card = second.pop(0)
    if first_card > second_card:
        if first_card == 9 and second_card == 0:
            second.append(first_card)
            second.append(second_card)
        else:
            first.append(first_card)
            first.append(second_card)
    if second_card > first_card:
        if first_card == 0 and second_card == 9:
            first.append(first_card)
            first.append(second_card)
        else:
            second.append(first_card)
            second.append(second_card)
    i += 1
if i <= 1000000:
    if len(first) == 0:
        print(f'second {i}')
    if len(second) == 0:
        print(f'first {i}')
else:
    print('botva')
