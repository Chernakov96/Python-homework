# Создайте программу для игры в ""Крестики-нолики"".
from typing import List
from typing import Optional

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


def draw_board(area: List) -> List:
    '''
    Функция, выводящая на консоль игровое поле из 9 пронумерованных клеток
    '''    
    print('│', area[1], '│', area[2], '│', area[3], '│')
    print('│', area[4], '│', area[5], '│', area[6], '│')
    print('│', area[7], '│', area[8], '│', area[9], '│')


def game(players: List, area: List) -> None:
    '''
    Логика игры
    arg players: список игроков
    arg area: список номеров клеток игрового поля
    '''   
    pl = players[0]
    for i in range(len(area) - 1):
        new_turn = 10
        while new_turn > 9 or area[new_turn] in ('X', 'O'):
            new_turn = give_int(
                f'{pl[1]}, куда поставить отметку? Введите число от 1 до 9:', 1)
            if new_turn > 9 or area[new_turn] in ('X', 'O'):
                print('Эта клетка уже занята\n')
        if pl == players[0]:
            area[new_turn] = 'X'
            draw_board(area)
            if i >= 4:
                check_win(area, players[0])
            pl = players[1]
        else:
            area[new_turn] = 'O'
            draw_board(area)
            if i >= 4:
                check_win(area, players[1])
            pl = players[0]


def check_win(area: List, players: List) -> None:
    '''
    Функция, проверяющая выигрышные комбинации
    arg players: список игроков
    arg area: список номеров клеток игрового поля
    '''   
    if area[1] == area[2] == area[3]\
            or area[4] == area[5] == area[6]\
            or area[7] == area[8] == area[9]\
            or area[1] == area[4] == area[7]\
            or area[2] == area[5] == area[8]\
            or area[3] == area[6] == area[9]\
            or area[1] == area[5] == area[9]\
            or area[3] == area[5] == area[7]:
        return exit(print(f'{players[1]} победил!'))
    else:
        return


area = list(range(10))
pl1 = input('Введите имя первого игрока:\n')
pl2 = input('Введите имя второго игрока:\n')
players = [[1, pl1], [2, pl2]]
draw_board(area)
game(players, area)