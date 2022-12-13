# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 150 конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from typing import Optional
from typing import List
from random import randint

def give_int(input_string: str, min_num: Optional[int] = None, max_num: Optional[int] = None) -> int:
    '''
    Takes an int number from user
    Takes: string
    Returns: int number or a message about an error
    '''
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше{min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите больше{max_num}')
                continue
            return num
        except ValueError:
            print('Вы ввели не число')

def player_logic(player_name: str, turn_limitation: int = 28, num: int = 74) -> int:

    sweet = 0
    while not 0 < sweet <= turn_limitation:
        sweet = give_int(
            f'{player_name}, сколько конфет вы хотите взять?\n', 1)
        if sweet > turn_limitation:
            print(f'Вы не можете взять больше, чем{turn_limitation}')
        elif sweet > num:
            print(f'Вы не можете взять больше, чем{num}')

    return sweet


def bot_logic(player_name: str, turn_limitation: int = 28, num: int = 74) -> int:
    sweet = 0
    if player_name == 'Hard Bot':
        if num <= turn_limitation:
            sweet = num
        else:
            if num % turn_limitation > 1:
                sweet = turn_limitation - 1
            else:
                sweet = turn_limitation - turn_limitation + 1
    elif player_name == 'Easy Bot':
        if num <= turn_limitation:
            sweet = num
        else:
            sweet = randint(1, 28)
    print(f'{player_name} берет {sweet} конфет')
    return sweet


def turn_maker(player_tuple: List[tuple], number: int = 74) -> None:
    first_turn = randint(0, 1)
    while number != 0:
        if player_tuple[first_turn][2] == 'man':
            sweet_amount = player_logic(
                player_name=player_tuple[first_turn][1], num=number)
        elif player_tuple[first_turn][2] == 'bot':
            sweet_amount = bot_logic(
                player_name=player_tuple[first_turn][1], num=number)
        number -= sweet_amount
        print(f'осталось {number} конфет\n')
        if number <= 0:
            exit(print(f'Победил {player_tuple[first_turn][1]}'))
        else:
            if first_turn:
                first_turn = 0
            else:
                first_turn = 1


def menu_input() -> None:
    while True:
        print('Нажмите 1 для игры вдвоем')
        print('Нажмите 2 для игры против бота')
        print('Нажмите -1 для выхода')
        num = input('Введите цифру:\n')
        if num == '1':
            pl_list = [(0, input('Введите имя первого игрока:\n'), 'man'),
                       (1, input('Введите имя второго игрока:\n'), 'man')]
            turn_maker(pl_list)
        elif num == '2':
            level = 0
            while level not in (1, 2):
                level = give_int('Выберите сложность бота\n'
                                 '1 - сложный\n'
                                 '2 - простой\n', 1)
                if level > 2:
                    print('Попробуйте еще  раз')
            if level == 1:
                pl_list = [(0, input('Введите имя первого игрока:\n'), 'man'),
                           (1, 'Hard Bot', 'bot')]
            else:
                pl_list = [(0, input('Введите имя первого игрока:\n'), 'man'),
                           (1, 'Easy Bot', 'bot')]
            turn_maker(pl_list)
        elif num == '-1':
            return exit(print('Вы вышли из игры'))
        else:
            print('Попробуйте еще раз')


menu_input()