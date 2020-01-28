#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

# ~ """
# ~ Программистский словарь
# ~ map(int , list) - применить int ко всем элементам list.
# ~ lambda x: 1 if x+3 in n_list else 0 - ф-ция без названия: x = 1 если x+3 in n_list, в противном случае x = 0. Пример использования n_list_new = map(lambda x: 1 if x+3 in n_list else 0, n_list)
# ~ list = [x for x in range(n)] - списковая сборка, на выходе получается спиок чисел от 0 до n.
# ~ " ".join((map(str, list_int)) - получу строку, в которой будут все целые чила из списка list_int через пробел(join принимает на вход только список строк).

import sys
import math

#Наибольший общий делитель двух чисел Фибоначчи равен числу Фибоначчи с индексом, равным наибольшему общему делителю индексов!!!

f_input = sys.stdin.read().strip().split(" ")
numb_i = int(f_input[0])
numb_j = int(f_input[1])

#находит число Фибоначи по его номеру - 1(по формуле Спивака)
def find_nF_number(number_task):
    number = number_task + 1
    a = (1 + math.sqrt(5)) / 2
    b = (1 - math.sqrt(5)) / 2
    nF = ((a**number - b**number) / math.sqrt(5)) % (10**9)
    return(int(nF))

#найдём НОД индексов
nod_i_j = math.gcd(numb_i, numb_j)
# Просто в лоб ищу число Ф как нормальные люди
def just_search_nF(numb):
    f0 = 0
    f1 = 1
    f2 = 1
    for i in range(numb-1):
        f2 = (f0 + f1) % 10**9
        f0, f1 = f1, f2
    return(f2)

#число Фибоначчи с индексом, равным наибольшему общему делителю индексов(nod_i_j-1)
print(just_search_nF(nod_i_j))
