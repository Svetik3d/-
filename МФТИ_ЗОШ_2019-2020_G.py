#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

"""
Программистский словарь
map(int , list) - применить int ко всем элементам list.
lambda x: 1 if x+3 in n_list else 0 - ф-ция без названия: x = 1 если x+3 in n_list, в противном случае x = 0. Пример использования n_list_new = map(lambda x: 1 if x+3 in n_list else 0, n_list)
list = [x for x in range(n)] - списковая сборка, на выходе получается спиок чисел от 0 до n.
" ".join((map(str, list_int)) - получу строку, в которой будут все целые чила из списка list_int через пробел(join принимает на вход только список строк).

"""

import sys

f_str = sys.stdin.read()
f = f_str.split(" ")

if "." in f_str:
    point_x = float(f[0])
    point_y = float(f[1])
    start_x = float(f[2])
    start_y = float(f[3])
    finish_x = float(f[4])
    finish_y = float(f[5])
else:
    point_x = int(f[0])
    point_y = int(f[1])
    start_x = int(f[2])
    start_y = int(f[3])
    finish_x = int(f[4])
    finish_y = int(f[5])

#Если векторы заданы своими координатами a(x1, y1), b(x2, y2) то скалярное произведение (a, b) = x1x2 + y1y2. Вектор повернут в сторону луча(угол между ними < 90)
scalar_pr = (point_x - start_x)*(finish_x - start_x) + (point_y - start_y)*(finish_y - start_y)
#Если векторы заданы своими координатами a(x1, y1), b(x2, y2) то косое произведение [a, b] = x1y2 — x2y1. Если оно =0, то векторы коллинеарны.
skew_pr = (point_x - start_x)*(finish_y - start_y) - (finish_x - start_x)*(point_y - start_y)

#отладка
#print("(point_x - start_x) ", (point_x - start_x), ", (point_y - start_y) = ", (point_y - start_y), ", (finish_y - start_y) = ",  (finish_y - start_y), ", (finish_x - start_x) = ", (finish_x - start_x), ", skew_pr = ", skew_pr, " scalar_pr = ", scalar_pr)



#Точка лежит на прямой если....
if (skew_pr == 0) and (scalar_pr >= 0):
    print("YES")
else:
    print("NO")
