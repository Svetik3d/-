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

sum_of = int(sys.stdin.read())

#ПЕРВЫЙ ВАРИАНТ

#проверяет 
# ~ def my_check(del_ch, del_zn):
    # ~ for r in del_ch:
        # ~ #print(str(del_ch), " ", del_zn)
        # ~ if r in del_zn:
            # ~ #print("Error!")
            # ~ return("Error!")

#ищет все делители числа
# ~ def my_del(a):
    # ~ answer_l = []
    # ~ for e in range(2, int(a/2)+1, 1):
        # ~ if (a % e) == 0:
            # ~ answer_l.append(e)
    # ~ answer_l.append(a)
    # ~ #print(str(a), " ", answer_l)
    # ~ return(answer_l)

# ~ def search(sum_):
    # ~ for i in range(sum_- 1):
        # ~ if (sum_ % 2) == 0:
            # ~ chis = int(sum_/ 2 - i)
            # ~ zn = int(sum_/ 2 + i)
        # ~ else:
            # ~ chis = int(sum_/ 2) - i
            # ~ zn = sum_ - chis
            # ~ if (chis / zn) != 1:
                # ~ return(" ".join(map(str,[chis,zn])))
        # ~ if (list(set(my_del(chis)) & set(my_del(zn))) == []) and ((chis / zn) != 1):
            # ~ return(" ".join(map(str,[chis,zn])))

#ВТОРОЙ ВАРИАНТ

# ~ def search(sum_):
    # ~ for i in range(sum_- 1):
        # ~ a = True
        # ~ if (sum_ % 2) == 0:
            # ~ chis = int(sum_/ 2 - i)
            # ~ zn = int(sum_/ 2 + i)
        # ~ else:
            # ~ chis = int(sum_/ 2) - i
            # ~ zn = sum_ - chis
        # ~ for e in range(2, int(chis/2)+1, 1):
            # ~ print(zn, chis, zn % chis)
            # ~ if (((chis % e) == 0) and ((zn % e) == 0)):
                # ~ a = False 
                # ~ break
        # ~ if (zn % chis) == 0:
            # ~ a = False
        # ~ if (a != False) and ((chis / zn) != 1):
            # ~ return(" ".join(map(str,[chis,zn])))

#НЕМНОГО ПОДУМАЛА И НАШЛА МАТЕМАТИЧЕСКУЮ ЗАКОНОМЕРНОСТЬ

def search(sum_):
    if (sum_ % 2) != 0:
        chis = int(sum_/ 2)
        zn = sum_ - chis
        return(" ".join(map(str,[chis,zn])))
    else:
        chis = int(sum_/ 2) - 1
        zn = sum_ - chis
        if (chis % 2) == 0:
            return(" ".join(map(str,[chis-1,zn+1])))
        else:
            return(" ".join(map(str,[chis,zn])))

print(search(sum_of))


