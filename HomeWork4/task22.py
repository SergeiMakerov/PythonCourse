# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


n = int(input('Введите кол-во элементов первого неупорядоченного набора целых чисел: '))
m = int(input('Введите кол-во элементов второго неупорядоченного набора целых чисел: '))
set_n = []
set_m = []
for i in range(n):
    x = int(input('Введите элемент первого набора чисел: '))
    set_n.append(x)
for i in range(m):
    x = int(input('Введите элемент второго набора чисел: '))
    set_m.append(x)

intersection = list(set(set_n) & set(set_m))
print(sorted(intersection))