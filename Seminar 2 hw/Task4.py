# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. 
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты. 
# Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. 
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. 
# Составьте алгоритм, который проводит эту игру. 
# Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep. 
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.
import random

number_of_players = int(input("Введите количество игроков: \n"))
countdown = random.randint(0, number_of_players)
before_countdown = 1
after_countdown = 2
list_of_players = [0] * number_of_players
print(list_of_players)

for j in range(0, number_of_players):
    for i in range(0, countdown):
        list_of_players[i] = list_of_players[i] + before_countdown
    for i in range(countdown, number_of_players):
        list_of_players[i] = list_of_players[i] + after_countdown
    print(list_of_players)
    list_of_players[countdown] += list_of_players[countdown-1] 
    list_of_players[countdown-1] = 0
    print(list_of_players)




