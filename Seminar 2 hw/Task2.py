# 2 - Напишите программу, которая
# 1. принимает на вход число N и
# 2. выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

number_of_elems = int(input("Пожалуйста введите целое положительное число: \n"))
if number_of_elems <= 0:
    print ('Вы ввели отрицательное число или ноль. Попробуйте ввести целое положительное число')
factorial = 1
list_factorial = []

for i in range(1, number_of_elems + 1):
    factorial *= i
    list_factorial.append(factorial)

print(list_factorial)
