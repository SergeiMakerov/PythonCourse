# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
list = [random.randint(0, 10) for i in range(20)]
print(list)
min_number = int(input())
max_number = int(input())
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)