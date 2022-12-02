
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random


def create_random_list(num):
    new_list = []
    for number in range(num):
        new_list.append(random.randint(0, 9))
    return new_list


def SumEvenElements(list):
    result = 0
    for i in range(len(list)):
        if i % 2 == 1:
            result += list[i]
    return result


amount_of_elements = int(input('Какого размера сгенерировать массив: \n'))
my_list = create_random_list(amount_of_elements)
print(my_list)
summ_elements = SumEvenElements(my_list)
print(summ_elements)

