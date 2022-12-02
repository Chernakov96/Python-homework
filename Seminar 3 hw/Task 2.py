# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
import random

def create_random_list(num):
    """
    Creates a list filled with positive random numbers from 0 to 9.
    
    Args:
        num - length of the list, decided by user
    Returns: 
        list 
    """ 
    new_list = []
    for number in range (num):
        new_list.append(random.randint(0,9))
    return new_list

def multiply_pairs(default_list):
    """
    Multiplies pairs in list(pair is first element and last, second element and second to last etc...).
    
    Args:
        default_list - list that was previously created
    Returns: 
        list 
    """ 
    result = []
    if int(len(default_list))%2 == 0:
        for number in range(int(len(default_list) / 2)):
            result.append(default_list[number] * default_list[(len(default_list) - 1) - number])
    else:
        for number in range(int(len(default_list)/ 2) + 1):
            result.append(default_list[number] * default_list[(len(default_list) - 1) - number])
    return result

amount_of_elements = int(input('Какого размера сгенерировать массив: \n'))
user_list = create_random_list(amount_of_elements)
print(user_list)
list_of_pairs = multiply_pairs(user_list)
print(list_of_pairs)
