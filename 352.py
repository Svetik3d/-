# https-acmp.ru
Задания олимпиадные по программированию
#352
#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai
"""
map(int , list) - применить int ко всем элементам list.
lambda x: 1 if x+3 in n_list else 0 - ф-ция без названия: x = 1 если x+3 in n_list, в противном случае x = 0. Пример использования n_list_new = map(lambda x: 1 if x+3 in n_list else 0, n_list)
list = [x for x in range(n)] - списковая сборка, на выходе получается спиок чисел от 0 до n.
" ".join((map(str, list_int)) - получу строку, в которой будут все целые чила из списка list_int через пробел(join принимает на вход только список строк).

"""


import sys

SUM = int(sys.stdin.read())

#НЕМНОГО ПОДУМАЛА И НАШЛА МАТЕМАТИЧЕСКУЮ ЗАКОНОМЕРНОСТЬ
def search(sum_):
    #если число чётное
    if (sum_ % 2) != 0:
        chis = int(sum_ / 2)
        znam = sum_ - chis
        return " ".join(map(str, [chis, znam]))
    #если число нечётное
    chis = int(sum_ / 2) - 1
    znam = sum_ - chis
    if (chis % 2) == 0:
        return " ".join(map(str, [chis-1, znam+1]))
    return " ".join(map(str, [chis, znam]))

print(search(SUM))


