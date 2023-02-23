deque = []
deque_size = 0

command = input()

while command != 'exit':
    if command.find('push_front') == 0:
        element = command.split(' ')
        deque.insert(0, element[1])
        deque_size += 1
        print('ok')
    if command.find('push_back') == 0:
        element = command.split(' ')
        deque.append(element[1])
        deque_size += 1
        print('ok')
    if command == 'pop_front':
        if deque_size <= 0:
            print('error')
        else:
            print(deque.pop(0))
            deque_size -= 1
    if command == 'pop_back':
        if deque_size <= 0:
            print('error')
        else:
            print(deque.pop(-1))
            deque_size -= 1
    if command == 'front':
        if deque_size <= 0:
            print('error')
        else:
            print(deque[0])
    if command == 'back':
        if deque_size <= 0:
            print('error')
        else:
            print(deque[-1])
    if command == 'size':
        print(deque_size)
    if command == 'clear':
        deque_size = 0
        deque = []
        print('ok')
    command = input()
print('bye')
