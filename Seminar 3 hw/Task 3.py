# 3-Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

import random


def create_random_list(num):
    """
    Creates a list filled with positive random floats with up to three numbers in fractional part.
    
    Args:
        num - length of the list, decided by user
    Returns: 
        list 
    """ 
    result_list = []
    for i in range(num):
        f = random.uniform(0, 9)
        fl_part = random.randint(1, 3)
        result_list.append(round(f, fl_part))
    return result_list

def float_side(num):
    """
    Finds float part of the element.
    
    Args:
        num - an element of list
    Returns: 
        rounded float 
    """ 
    result = num - int(num)
    return round(result, 3)


def diff_min_max_float(list):
    """
    Finds the difference between the largest floating part and the smallest floating part 
    of the element in the list.
    
    Args:
        list - list with floats created by user
    Returns: 
        float - the difference between max and min float numbers 
    """ 
    min_float = float_side(list[0])
    max_float = float_side(list[0])

    for i in range(len(list)):
        if float_side(list[i]) > max_float:
            max_float = float_side(list[i])
        if float_side(list[i]) < min_float:
            min_float = float_side(list[i])

    result = (max_float - min_float)
    return round(result, 3)

number = int(input('Введите размер списка \n'))
my_list = create_random_list(number)
print(my_list)
diff_float = diff_min_max_float(my_list)
print(f'Разница - {diff_float}')