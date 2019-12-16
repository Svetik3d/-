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
import time

f_str = sys.stdin.read().split("\n")

if f_str[-1] == "":
    del f_str[-1]

f_int = list(map(int, f_str))
t = f_int[0]
del f_int[0]

#возвращает число обратное a mod m, a и m - взаимно простые
def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
    if (m == 1) : 
        return 0
    while (a > 1) : 
        q = a // m 
        t = m 
        m = a % m 
        a = t 
        t = y 
        y = x - q * y 
        x = t 
    if (x < 0) : 
        x = x + m0 
    return x 

for a in f_int:
    print(modInverse(a,(10**9 + 9)))
