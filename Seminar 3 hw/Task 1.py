
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
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
    for number in range(num):
        new_list.append(random.randint(0, 9))
    return new_list


def SumEvenElements(list):
    """
    Sums up every odd element of the list.
    
    Args:
        list - a list, from which the selection would be performed
    Returns: 
        list of odd numbers
    """ 
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

