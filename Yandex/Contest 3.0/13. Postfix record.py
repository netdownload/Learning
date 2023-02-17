i = input().rstrip().split(' ')
stack = []

for elem in i:
    if elem != '+' and elem != '-' and elem != '*':
        stack.append(elem)
    else:
        l = int(stack.pop())
        f = int(stack.pop())
        if elem == '+':
            stack.append(f + l)
        if elem == '-':
            stack.append(f - l)
        if elem == '*':
            stack.append(f * l)
print(stack.pop())
