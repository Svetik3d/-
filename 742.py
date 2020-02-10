#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

# ~ """
# ~ Программистский словарь
# ~ map(int , list) - применить int ко всем элементам list.
# ~ lambda x: 1 if x+3 in n_list else 0 - ф-ция без названия: x = 1 если x+3 in n_list, в противном случае x = 0. Пример использования n_list_new = map(lambda x: 1 if x+3 in n_list else 0, n_list)
# ~ list = [x for x in range(n)] - списковая сборка, на выходе получается спиок чисел от 0 до n.
# ~ " ".join((map(str, list_int)) - получу строку, в которой будут все целые чила из списка list_int через пробел(join принимает на вход только список строк).

#Способ получения алфавита
# ~ a = ord('а')
# ~ for i in range(a,a+32):
    # ~ alfvt.append(chr(i))
# ~ print(alfvt)

import sys
import math


n = int(sys.stdin.read().strip())

stepen = n*(n-1)/2
answer = pow(3, int(stepen))
print(int(answer))
