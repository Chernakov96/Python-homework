# A. Задана натуральная степень k. 
# 1. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# 2. и записать в файл многочлен степени k.
# Пример:
# # если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random


def EquationGenerateToDict(k):
    result_dict = {}
    for i in range(k + 1):
        result_dict[i] = random.randint(0, 2)
    return result_dict


def EquationConvertToDict(equation):
    equation = equation.replace(' ', '')
    equation = equation[:-2].split('+')
    new_equation = {}
    for i in range(len(equation)):
        temp_var = equation[i].split('X')
        if len(temp_var) != 1:  # Если есть степень
            if temp_var[1] == '':  # первая степень
                if temp_var[0] == '':  # если коэффициент равен единице
                    new_equation['1'] = '1'
                else:  # если коэффициент не равен единице
                    new_equation['1'] = temp_var[0].replace('*', '')
            else:  # не первая степень
                if temp_var[0] == '':  # если коэффициент равен единице
                    new_equation[temp_var[1].replace('*', '')] = '1'
                else:  # если коэффициент не равен единице
                    new_equation[temp_var[1].replace('*', '')] = temp_var[0].replace('*', '')
        else:
            new_equation['0'] = temp_var[0]

    return new_equation


def EquationConvertToStr(equation_dict):
    equation_string = ''
    for i in range(len(equation_dict) - 1, -1, -1):
        if equation_dict[i] != 0:
            if i > 1:
                if equation_dict[i] != 0:
                    if equation_dict[i] == 1:
                        equation_string += f'X**{i} '
                    else:
                        equation_string += f'{equation_dict[i]}*X**{i} '
            elif i == 1:
                if equation_dict[i] != 0:
                    if equation_dict[i] == 1:
                        equation_string += f'X '
                    else:
                        equation_string += f'{equation_dict[i]}*X '
            elif i == 0:
                if equation_dict[i] != 0:
                    equation_string += f'{equation_dict[i]} '
        if i == 0:
            equation_string += f' = 0'
        elif equation_string != '' and equation_dict[i - 1] != 0:
            equation_string += f'+ '

    return equation_string


def NormalizeDictMaxPow(equation, max_pow):
    for i in range(int(max_pow) + 1):
        if equation.get(str(i)) is None:
            equation[str(i)] = '0'
        else:
            equation[str(i)] = equation[str(i)]

    return equation


def EquationSummToStr(equation_1, equation_2):
    result_dict = {}
    result_str = ''
    temp_1 = EquationConvertToDict(equation_1)
    temp_2 = EquationConvertToDict(equation_2)
    if max(list(temp_1.keys())) >= max(list(temp_2.keys())):
        max_pow = max(list(temp_1.keys()))
    else:
        max_pow = max(list(temp_2.keys()))
    temp_1 = NormalizeDictMaxPow(temp_1, max_pow)
    temp_2 = NormalizeDictMaxPow(temp_2, max_pow)
    for i in range(len(temp_1)):
        result_dict[int(i)] = int(temp_1[str(i)]) + int(temp_2[str(i)])

    result_str = EquationConvertToStr(result_dict)
    return result_str


equation_str_1 = EquationConvertToStr(EquationGenerateToDict(3))
print(f'Первое уравнение: {equation_str_1}')
equation_dict_1 = EquationConvertToDict(equation_str_1)
equation_str_2 = EquationConvertToStr(EquationGenerateToDict(3))
print(f'Второе уравнение: {equation_str_2}')
result_summ = EquationSummToStr(equation_str_1, equation_str_2)
print(result_summ)
# Запись и создание файла
with open('file.txt', 'a', encoding='UTF-8') as data:
    data.write(f'Первое уравнение: {equation_str_1}\n')
    data.write(f'Второе уравнение: {equation_str_2}\n')
    data.write(f'Сумма многочленов: {result_summ}\n')
    data.write(f'\n')
