# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному 
# числу X. Пользователь в первой строке вводит натуральное число N – количество элементов 
# в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Введите колличество элементов N: "))
l = list(range(1, n + 1))
x = int(input("Введите число X: "))

print(f'n = {n}')
result = 0
for i in range(n + 1):
    if abs(i - x) < abs(result - x):
        result = i
print(*l)
print(f'x = {x}')
print(f'-> {result} ')
print(" ")