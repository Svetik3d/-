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

f_str = sys.stdin.read().split(" ")
f = list(map(int , f_str))

w = f[0]
h = f[1]
d = f[2]

s_window = (w-2*d)*(h-2*d)

#Отладка
#print(w, " ", h, " ", d, " ", (w-2*d), " ", (h-2*d))

if (s_window <= 0) or ((w-2*d)<0) or ((h-2*d)<0):
    print(0)
else:
    print(s_window)
