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

f_str = sys.stdin.read().strip()

str_l = list(f_str)

#превращаю list в dict где ключи - значения list, а значения - кол-во их повторений в строке

def dct(a, str_with_a):
    akk = 0
    for i in str_with_a:
        if i == a:
            akk = akk + 1
    return akk

str_d = {}

for i in set(str_l):
    str_d[i] = dct(i, f_str) % 2

str_s = set(str_d.values())

if str_s == {0}:
    print("even")
elif str_s == {1}:
    print("odd")
else:
    print("neither")

