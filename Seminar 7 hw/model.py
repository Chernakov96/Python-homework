first_number = 0
intermediate_result = 0
next_number = 0
calc_string = ''

def summa() -> int:
    global intermediate_result
    global next_number
    global first_number
    intermediate_result = first_number + next_number
    first_number = intermediate_result


def difference() -> int:
    global intermediate_result
    global next_number
    global first_number
    intermediate_result = first_number - next_number
    first_number = intermediate_result


def multiplication()-> int:
    global intermediate_result
    global next_number
    global first_number
    intermediate_result = first_number * next_number
    first_number = intermediate_result


def division()-> int:
    global intermediate_result
    global next_number
    global first_number
    intermediate_result = first_number / next_number
    first_number = intermediate_result


def check_operation(sm_operation: str):
    if sm_operation == '+':
        summa()
    elif sm_operation == '-':
        difference()
    elif sm_operation == '*':
        multiplication()
    elif sm_operation == '/':
        division()

def get_intermediate_result():
    global intermediate_result
    return intermediate_result

def set_intermediate_result(smth):
    global intermediate_result
    intermediate_result = smth

def set_next_number(smth):
    global next_number
    next_number = smth

def get_next_number():
    global next_number
    return next_number

def get_first_number():
    global first_number
    return first_number

def set_first_number(smth):
    global first_number
    first_number = smth

def get_calc_string():
    global calc_string
    return calc_string

def set_calc_string(smth):
    global calc_string
    calc_string = smth

def calculate_str(sm_str) -> int:
    sm_list = sm_str.split()
    for i in range(len(sm_list)):
        if sm_list[i].isdigit():
            sm_list[i] = int(sm_list[i])
    while ('*' in sm_list) or ('/' in sm_list):
        i = 0
        while i < len(sm_list):
            if sm_list[i] == "*":
                sm_list[i-1] = sm_list[i-1] * sm_list[i+1]
                sm_list.remove(sm_list[i])
                sm_list.remove(sm_list[i])

            elif sm_list[i] == "/":
                sm_list[i-1] = sm_list[i-1] / sm_list[i+1]
                sm_list.remove(sm_list[i])
                sm_list.remove(sm_list[i])

            else:
                i += 1

    while ('+' in sm_list) or ('-' in sm_list):
        i = 0
        while i < len(sm_list):
            if sm_list[i] == "+":
                sm_list[i-1] = sm_list[i-1] + sm_list[i+1]
                sm_list.remove(sm_list[i])
                sm_list.remove(sm_list[i])

            elif sm_list[i] == "-":
                sm_list[i-1] = sm_list[i-1] - sm_list[i+1]
                sm_list.remove(sm_list[i])
                sm_list.remove(sm_list[i])
            else:
                i += 1

    return sm_list[0]