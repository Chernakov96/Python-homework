

def input_number():
    number = int(input('Enter the number:\n'))
    return number

def input_operation():
    operation = input('Enter the operation(+, -, *, /, =):\n ')
    return operation

def print_result(smth):
    print(smth)

def input_string():
    calc_string = input('Enter the string:  ')
    calc_string = calc_string.replace(' ', '')
    if '=' in calc_string:
        calc_string = calc_string[:calc_string.find('=')]
    calc_string = calc_string.replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ')
    return calc_string

def input_calc_type():
    answer = input('Choose calc type: \n О - Console calc \n 1  - String calc  \n')
    while answer not in ['0', '1']:
        answer = input('Error. Try again: \n О - Console calc, \n 1  - String calc  \n')
    return int(answer)