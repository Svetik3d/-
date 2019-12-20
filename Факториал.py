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
import math

sys.setrecursionlimit(15000)

n = int(sys.stdin.read())

#v1 - Accepted
factorial = 1
for i in range(1, n + 1, 1):
    factorial = i * factorial
print(factorial)

#v2 - Accepted
print(math.factorial(n))

#v3, на больших числах в проверяющей системе, а у меня на компе работает даже с максимальным значением(N < 1000)
def factorial(number):
    if number == 1:
        return(1)
    else:
        return(number * factorial(number - 1))
print(factorial(n))
