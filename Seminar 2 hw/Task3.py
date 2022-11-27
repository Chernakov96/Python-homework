# 3 - Дан массив размера N.
# 0. После каждого отрицательного элемента массива
# 1. вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]
import random

list_number_of_elements = int(
    input(
        "Пожалуйста введите количество элементов в массиве(целым положительным числом): \n"
    ))
if list_number_of_elements <= 0:
    print(
        "Вы ввели ноль либо отрицательное число. Пожалуйста введите целочисленное положительное число"
    )

random_list = []
for i in range(0, list_number_of_elements):
    random_number = random.randint(-30, 30)
    random_list.append(random_number)
print(random_list)

new_random_list = []
for each in random_list:
    new_random_list.append(each)
    if each < 0:
        new_random_list.append(0)
print(new_random_list)

