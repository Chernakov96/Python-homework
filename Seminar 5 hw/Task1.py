# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def delete_element(input_string):
    '''
    The function splits string into words and then constructs a new list
    which does not contain words you want to delete
    '''
    to_delete = input('Type string you want to remove:\n>> ') #Type ""абв"" here to delete all words containing ""абв""
    result_list = [i for i in input_string.split() if to_delete not in i]
    return ' '.join(result_list)

result = delete_element(input('Type some text:\n>> '))
print(result)
