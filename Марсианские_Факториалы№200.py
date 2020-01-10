#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

# ~ """
# ~ Программистский словарь
# ~ map(int , list) - применить int ко всем элементам list.
# ~ lambda x: 1 if x+3 in n_list else 0 - ф-ция без названия: x = 1 если x+3 in n_list, в противном случае x = 0. Пример использования n_list_new = map(lambda x: 1 if x+3 in n_list else 0, n_list)
# ~ list = [x for x in range(n)] - списковая сборка, на выходе получается спиок чисел от 0 до n.
# ~ " ".join((map(str, list_int)) - получу строку, в которой будут все целые чила из списка list_int через пробел(join принимает на вход только список строк).

# ~ """

###############V1 - TimeLimit###############

# import math
# import sys

# def translate_from_10_in_any(number, o_sys_sch):
    # all_s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'           
    # r = ''
    # while number:
        # number, y = divmod(number, o_sys_sch) 
        # r = all_s[y]+r
    # return r

# def podschet_nole(n, d, akk):
    # a = True
    # while a:
        # if n%10**d == 0:
            # #print(n, d, akk)
            # n /= 10**d
            # akk += d
            # #print(n, d, akk)
        # else:
            # if d != 1:
                # akk += podschet_nole(n, int(d/2), akk)
            # a = False
    # return(akk)

# f = sys.stdin.read().strip().split(" ")
# k = int(f[0])
# osnov = int(f[1])
# m_f = int(translate_from_10_in_any(math.factorial(k), osnov))

# print(podschet_nole(m_f, len(str(int(m_f/2))), 0))

###############V2 - Accepted###############

import sys
import math

def dct_add(el, dct):
    if el in dct.keys():
        dct[el] = dct[el] + 1
    else:
        dct[el] = 1

def Factor(n):
   Ans = []
   d = 2
   while d * d <= n:
       if n % d == 0:
           Ans.append(d)
           n //= d
       else:
           d += 1
   if n > 1:
       Ans.append(n)
   return Ans

f = sys.stdin.read().strip().split(" ")
n = int(f[0])
b = int(f[1])
p_mn_b = {}
answr_l = []

simple_n_l =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

#заполнить p_mn_b простыми множителями b так, что ключи - сами множители, заначение - сколько раз встречается множитель
# for i in range(1, int(math.sqrt(b) + 1), 1):
    # c = b % i
    # d = b // i
    # if (c == 0) and (i in simple_n_l):
        # dct_add(i, p_mn_b)
        # if (i != d) and (d in simple_n_l):
            # dct_add(d, p_mn_b)

#заполнить p_mn_b простыми множителями b так, что ключи - сами множители, заначение - сколько раз встречается множитель
p_mn_b_l = Factor(b)
for i in p_mn_b_l:
    dct_add(i, p_mn_b)

#Основной алгоритм
#print("p_mn_b.keys()) = ", p_mn_b.keys())
for k in p_mn_b.keys():
    #print("k = ", k)
    answr = 0
    for i in range(1, n, 1):
        if int(n / (k**i)) != 0:
            #print("int(n / (k**i) = ", int(n / (k**i)))
            answr += int(n / (k**i))
        else:
            break
    #print(int(answr / p_mn_b[k]))
    answr_l.append(int(answr / p_mn_b[k]))

print(min(answr_l))
