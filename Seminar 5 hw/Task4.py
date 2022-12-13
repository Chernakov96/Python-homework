# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def stringCompression(input_data):
    result = ''
    prev_char = input_data[0]
    count = 0
    for i in range(len(input_data)):
        if input_data[i] == prev_char:
            count += 1
        else:
            result += f'{count}{prev_char}'
            prev_char = input_data[i]
            count = 1
        if i == len(input_data) - 1:
            result += f'{count}{prev_char}'
    return result


def StringUnpacking(comp_str):
    result = ''
    count = ''
    for i in range(len(comp_str)):
        if comp_str[i].isdigit():
            count += comp_str[i]
        else:
            char = comp_str[i] * int(count)
            result += char
            count = ''
    return result


with open('Task4_input.txt', 'r', encoding='UTF-8') as data:
    inp_string = data.readline()

with open('Task4_output.txt', 'a', encoding='UTF-8') as data:
    data.write(f'Исходная строка: {inp_string}\n')
    data.write(f'Сжатая строка: {stringCompression(inp_string)}\n')