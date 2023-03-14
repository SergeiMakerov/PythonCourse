n = int(input("Введите трехзначное число: "))

number1 = n // 100
number2 = (n // 10) % 10
number3 = n % 10

print("Сумма цифр числа:", number1 + number2 + number3)
