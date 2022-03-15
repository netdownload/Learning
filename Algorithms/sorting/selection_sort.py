LIST = [11, 3, 4, 5, 7, 8, 6, 2, 1, 5, 0]


def find_smallest(list):
    smallest_index = 0
    smallest = list[0]
    for _ in range(len(list)):
        if list[_] < smallest:
            smallest = list[_]
            smallest_index = _
    return smallest_index


def selection_sort(list):
    new_arr = []
    for _ in range(len(list)):
        smallest_index = find_smallest(list)
        new_arr.append(list[smallest_index])
        list.pop(smallest_index)
    return new_arr


print(selection_sort(LIST))
