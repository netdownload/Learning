# Задача с кодом. Сумма диапазона чисел
#
# Напишите функцию, которая будет принимать начальное и конечное число в диапазоне чисел и возвращать сумму всех
# чисел этого диапазона.
#
# Примеры
#
# sum_problem(-10, 1) ➞ -54
# sum_problem(-20, 5) ➞ -195
# sum_problem(90, 45) ➞ 3105


def sum_problem(num1, num2):
    sum = 0
    if num1 > num2:
        num1, num2 = num2, num1
    for _ in range(num1, num2+1):
        sum = sum + _
    return sum


print(sum_problem(90, 45))


# Решение с сайта
# def sum_problem(a, b):
#     return sum(range(min(a, b), max(a, b) + 1))

# def sum_problem(a, b):
#     return (a + b) * (abs(a - b) + 1) // 2
#
# (-10+1)*(abs(-10-1)+1) //2  -9*12//2 -108//2 = -54
# -15*26//2 = -195
