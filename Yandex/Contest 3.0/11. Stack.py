stack = []
stack_size = 0

command = input()
while command != 'exit':
    if command.find('push') == 0:
        push_element = command.split(' ')
        stack.append(push_element[1])
        stack_size += 1
        print('ok')
    if command == 'back':
        if stack_size > 0:
                print(stack[stack_size-1])
        else:
            print('error')
    if command == 'pop':
        if stack_size > 0:
            print(stack[stack_size-1])
            stack.pop()
            stack_size -= 1
        else:
            print('error')
    if command == 'size':
        print(stack_size)
    if command == 'clear':
        stack = []
        stack_size = 0
        print('ok')
    command = input()
print('bye')

