# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого.
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.
# Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга.
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге.
# Составьте алгоритм, который проводит эту игру.
# Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep.
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.
import random

#Первая идея по решению через один список
# number_of_players = int(input("Введите количество игроков: \n"))
# countdown = random.randint(1, number_of_players-1)
# before_countdown = 1
# after_countdown = 2
# list_of_players = [0] * number_of_players
# print(list_of_players)

# for j in range(0, number_of_players - 1):
#     for i in range(0, countdown):
#         list_of_players[i] = list_of_players[i] + before_countdown
#     for i in range(countdown, number_of_players):
#         list_of_players[i] = list_of_players[i] + after_countdown
#     print(list_of_players)
#     list_of_players[countdown] += list_of_players[countdown - 1]
#     list_of_players[countdown - 1] = 0
#     list_of_players.remove(0)
#     number_of_players = number_of_players - 1
#     print(list_of_players)

# Набросок с двумя списками
# number_of_players = int(input("Введите количество игроков: \n"))
# countdown = random.randint(1, number_of_players - 1)
# print(countdown)
# before_countdown = 1
# after_countdown = 2
# list_of_players = list(range(1, number_of_players + 1))
# list_of_money = [0] * number_of_players
# for each_player in range(countdown):
#     list_of_money[each_player] = list_of_money[each_player] + before_countdown
# for each_player in range(countdown, number_of_players):
#     list_of_money[each_player] = list_of_money[each_player] + after_countdown
# print(list_of_money)
# print(list_of_players)
# list_of_money[countdown] = list_of_money[countdown] + list_of_money[countdown-1]
# list_of_money[countdown-1] = 0
# print(list_of_money)
# print(list_of_players)
# list_of_money.remove(0)
# list_of_players[countdown-1] = 0
# print(list_of_money)
# print(list_of_players)
# First_half = list_of_players[:countdown]
# list_of_players = list_of_players[-countdown:] + First_half
# print(list_of_players)
# money_slice = list_of_money[:countdown+1]
# players_slice = list_of_players[:countdown+1]
# list_of_money = [money_slice] + list_of_money
# list_of_players = [players_slice] + list_of_players
# print(list_of_money)
# print(list_of_players)