# 5- Напишите программу, которая 
# 1. принимает на вход координаты двух точек и 
# 2. находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21
import math


A_dot_X = int(input('Введите целочисленное число, являющееся координатой Х первой точки \n'))
A_dot_Y = int(input('Введите целочисленное число, являющееся координатой Y первой точки \n'))
B_dot_X = int(input('Введите целочисленное число, являющееся координатой Х второй точки \n'))
B_dot_Y = int(input('Введите целочисленное число, являющееся координатой Y второй точки \n'))
result = float(round(math.sqrt((A_dot_X - B_dot_X ) ** 2 + (A_dot_Y - B_dot_Y) ** 2), 2))
print(result)