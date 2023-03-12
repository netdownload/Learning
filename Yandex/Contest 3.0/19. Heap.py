# def push_heap(heap, element):
#     heap.append(element)
#     pos = len(heap) - 1
#     while pos > 0 and heap[pos] > heap[(pos - 1) // 2]:
#         heap[pos], heap[(pos - 1) // 2] = heap[(pos - 1) // 2], heap[pos]
#         pos = (pos - 1) // 2
#
#
# def extract_heap(heap):
#     ans = heap[0]
#     pos = 0
#     pop_position = 0
#     while (2 * pos + 2) < len(heap):
#         if (2 * pos + 1) <= (len(heap) - 1) and (2 * pos + 2) <= (len(heap) - 1):
#             if heap[2 * pos + 1] > heap[2 * pos + 2]:
#                 heap[pos], heap[2 * pos + 1] = heap[2 * pos + 1], heap[pos]
#                 pop_position = 2 * pos + 1
#                 pos = 2 * pos + 1
#             else:
#                 heap[pos], heap[2 * pos + 2] = heap[2 * pos + 2], heap[pos]
#                 pop_position = 2 * pos + 2
#                 pos = 2 * pos + 2
#         elif (2 * pos + 1) <= (len(heap) - 1) < (2 * pos + 2):
#             if heap[pos] > heap[2 * pos + 1]:
#                 heap[pos], heap[2 * pos + 1] = heap[2 * pos + 1], heap[pos]
#                 pop_position = 2 * pos + 1
#         elif (2 * pos) == len(heap) - 1:
#             pop_position = pos
#     heap.pop(pop_position)
#     return ans
#
#
# heap = []
# command = int(input())
#
# for i in range(command):
#     command = input()
#     if command != '1':
#         element = command.split(' ')
#         push_heap(heap, int(element[1]))
#     if command == '1':
#         print(extract_heap(heap))

n = int(input())
arr = []
for _ in range(n):
    x = input().split()
    if len(x) == 1:
        print(arr[0])
        arr[0] = arr[len(arr)-1]
        arr.pop()
        i = 0
        while i*2+2 < len(arr):
            if arr[2*i+1] > arr[i] or arr[2*i+2] > arr[i]:
                if arr[2*i+1] > arr[2*i+2]:
                    arr[i], arr[2*i+1] = arr[2*i+1], arr[i]
                    i = 2*i+1
                else:
                    arr[i], arr[2*i+2] = arr[2*i+2], arr[i]
                    i = 2 * i + 2
            else:
                break
        if 2*i+1 < len(arr) and arr[2 * i + 1] > arr[i]:
            arr[i], arr[2 * i + 1] = arr[2 * i + 1], arr[i]
    else:
        tmp = int(x[1])
        arr.append(tmp)
        i = len(arr) - 1
        while i > 0 and arr[(i-1)//2] < arr[i]:
            arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
            i = (i - 1) // 2
