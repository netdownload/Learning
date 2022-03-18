#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Отец', 'Мать', 'Сияна']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Отец', 175],
    ['Мать', 175],
    ['Сияна', 140],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
family_height = 0
for _ in range(len(my_family_height)):
    if my_family_height[_][0] == "Отец":
        print('Рост отца - '+ str(my_family_height[_][1]) + ' см')
    family_height = family_height + my_family_height[_][1]

print('Общий рост моей семьи - ' + str(family_height) + ' см')
print(my_family_height)