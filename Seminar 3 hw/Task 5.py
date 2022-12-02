# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci_positive(num):
    if num in [1, 2]:
        return 1
    else:
        return fibonacci_positive(num - 1) + fibonacci_positive(num - 2)

def fibonacci_negative(num):
    if num == 1:
        return 1
    elif num == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for elements in range(2, num):
            num1, num2 = num2, num1 - num2
        return num2


def add_two_fibonacci(num):
    result = []
    result.append(0)
    for i in range(1, num + 1):
        result.append(fibonacci_positive(i))
        result.insert(0, fibonacci_negative(i))
    return result

number = int(input('Введите размер списка Фибоначчи: \n'))
print(add_two_fibonacci(number))