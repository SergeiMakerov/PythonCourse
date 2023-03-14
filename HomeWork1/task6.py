n = input('Введите шестизначный номер билета: ')

sum1 = int(n[0])+int(n[1])+int(n[2])
sum2 = int(n[3])+int(n[4])+int(n[5])

if sum1 == sum2:
    print('Счастливый билет')
else:
    print('Обычный билет')