# 1 - Напишите программу, которая 
# 1. принимает на вход вещественное число и 
# 2. показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

real_number = float(input("Введите дробное число через '.' "))
if real_number < 0:
    real_number *= -1

result = 0

for i in str(real_number):
    if i != '.':
        result += int(i)

print(result)
