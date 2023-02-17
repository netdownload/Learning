# binary search
# O = log2n
# На входе отсортированный массив
LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ITEM = 4


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(LIST, ITEM))
