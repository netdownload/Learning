queue = []
queue_size = 0

command = input()
while command != 'exit':
    if command.find('push') == 0:
        push_element = command.split(' ')
        queue.append(push_element[1])
        queue_size += 1
        print('ok')
    if command == 'front':
        if queue_size > 0:
            print(queue[0])
        else:
            print('error')
    if command == 'pop':
        if queue_size > 0:
            print(queue[0])
            queue.pop(0)
            queue_size -= 1
        else:
            print('error')
    if command == 'size':
        print(queue_size)
    if command == 'clear':
        queue = []
        queue_size = 0
        print('ok')
    command = input()
print('bye')
