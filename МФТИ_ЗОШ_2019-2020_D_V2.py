#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

"""
Программистский словарь python
map(int , list) - применить int ко всем элементам list.

lambda x: 1 if x+3 in n_list else 0 - ф-ция без названия: x = 1 если x+3 in
  n_list, в противном случае x = 0. Пример использования n_list_new =
  map(lambda x: 1 if x+3 in n_list else 0, n_list)

list = [x for x in range(n)] - списковая сборка, на выходе получается спиок
  чисел от 0 до n.

" ".join((map(str, list_int)) - получу строку, в которой будут все целые чила
  из списка list_int через пробел(join принимает на вход только список строк).
"""

import sys
#import resource

n_of = int(sys.stdin.read())
#sys.setrecursionlimit(15000)

dct = {}
max_d = 150

def put(n, start_i=0):
    l = []
    if n <= 2:
        if not n in dct.keys() and len(dct) < max_d:
            dct[n] = [n]
        return([n])
    else:
        for i in range(start_i, n, 1):
            if n - i > i:
                l.append([n - i, i])
            if i > 2:
                if i in dct.keys():
                    for d in dct[i]:
                        if n - i > d[0]:
                            l.append([n - i] + d)
                else:
                    put_i_l = put(i, 1)
                    for p in put_i_l:
                        if n - i > p[0]:
                            l.append([n - i] + p)
        if not n in dct.keys() and len(dct) < max_d:
            dct[n] = l
        return(l)

#print(put(n_of))
print(len(put(n_of)))
#print(resource.getrusage(resource.RUSAGE_SELF))
#print(dct)
